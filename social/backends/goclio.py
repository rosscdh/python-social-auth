"""
Angel OAuth2 backend, docs at:
    http://psa.matiasaguirre.net/docs/backends/angel.html
"""
from social.backends.oauth import BaseOAuth2


class GoClioOAuth2(BaseOAuth2):
    name = 'goclio'
    AUTHORIZATION_URL = 'https://app.goclio.com/oauth/authorize/'
    ACCESS_TOKEN_METHOD = 'POST'
    ACCESS_TOKEN_URL = 'https://app.goclio.com/oauth/token/'
    REDIRECT_STATE = False
    STATE_PARAMETER = False

    def get_user_details(self, response):
        """Return user details from GoClio account"""
        import pdb;pdb.set_trace()
        username = response['angellist_url'].split('/')[-1]
        email = response.get('email', '')
        fullname, first_name, last_name = self.get_user_names(response['name'])
        return {'username': username,
                'fullname': fullname,
                'first_name': first_name,
                'last_name': last_name,
                'email': email}

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        return self.get_json('https://app.goclio.com/api/v2/users/who_am_i', params={
            'access_token': access_token
        })