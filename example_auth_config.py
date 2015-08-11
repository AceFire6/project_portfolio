import authomatic

CONFIG = {
    'google': {
        'class_': authomatic.providers.oauth2.Google,
        'short_name': authomatic.short_name(),
        'consumer_key': 'google_client_id',
        'consumer_secret': 'google_client_secret',
        'scope': ['https://www.googleapis.com/auth/userinfo.profile',
                  'https://www.googleapis.com/auth/userinfo.email']
    },
}
