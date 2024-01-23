# Documentation-and-Samples

## Generating API Keys

API Keys are generated for an individual user.  That is, each user has a distinct pair of API Keys which distinctly identify them within the ThoughtRiver platform.

ThoughtRiver Support need to enable this feature on a customer by customer basis, so if you do not see the API Keys menu item below, please contact support:

![ThoughtRiver API Keys Menu](./docs/api_keys/api_keys_menu.png)

When you first select the API Keys menu item you will be shown a screen to generate your unique API Key pair:

![Generate API Keys Button](./docs/api_keys/generate_api_keys.png)

Clicking the Generate Keys button will generate a Primary and Secondary API Key.  Please make sure to save these keys as you will not be able to retrieve them after closing this page.  

![Copy Generated API Keys](./docs/api_keys/generated_api_keys.png)

Both the Primary and Secondary API keys allow you to access the ThoughtRiver API.  Your application should initially be configured to use the Primary API key.  At such time that you wish to rotate your API Keys as part of your security best practice you should first configure your application to use the Secondary API Key and then click the Rotate Keys button.  

![Rotate API Keys Button](./docs/api_keys/rotate_api_keys_button.png)

Rotating the keys will cause the Primary Key to be set to the Secondary Key and then the Secondary Key is assigned a new value.

![Copy rotated API Key Button](./docs/api_keys/rotated_api_key.png)
