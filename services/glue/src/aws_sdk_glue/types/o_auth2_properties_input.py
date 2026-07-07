"""Generated from Smithy shape ``com.amazonaws.glue#OAuth2PropertiesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.authorization_code_properties
    import aws_sdk_glue.types.o_auth2_client_application
    import aws_sdk_glue.types.o_auth2_credentials
    import aws_sdk_glue.types.o_auth2_grant_type
    import aws_sdk_glue.types.token_url
    import aws_sdk_glue.types.token_url_parameters_map


class OAuth2PropertiesInput(TypedDict, closed=True):
    o_auth2_grant_type: NotRequired[
        "aws_sdk_glue.types.o_auth2_grant_type.OAuth2GrantType"
    ]
    """<p>The OAuth2 grant type in the CreateConnection request. For example, <code>AUTHORIZATION_CODE</code>, <code>JWT_BEARER</code>, or <code>CLIENT_CREDENTIALS</code>.</p>"""
    o_auth2_client_application: NotRequired[
        "aws_sdk_glue.types.o_auth2_client_application.OAuth2ClientApplication"
    ]
    """<p>The client application type in the CreateConnection request. For example, <code>AWS_MANAGED</code> or <code>USER_MANAGED</code>.</p>"""
    token_url: NotRequired["aws_sdk_glue.types.token_url.TokenUrl"]
    """<p>The URL of the provider's authentication server, to exchange an authorization code for an access token.</p>"""
    token_url_parameters_map: NotRequired[
        "aws_sdk_glue.types.token_url_parameters_map.TokenUrlParametersMap"
    ]
    """<p>A map of parameters that are added to the token <code>GET</code> request.</p>"""
    authorization_code_properties: NotRequired[
        "aws_sdk_glue.types.authorization_code_properties.AuthorizationCodeProperties"
    ]
    """<p>The set of properties required for the the OAuth2 <code>AUTHORIZATION_CODE</code> grant type.</p>"""
    o_auth2_credentials: NotRequired[
        "aws_sdk_glue.types.o_auth2_credentials.OAuth2Credentials"
    ]
    """<p>The credentials used when the authentication type is OAuth2 authentication.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OAuth2PropertiesInput) -> dict:
    out: dict = {}
    if "o_auth2_grant_type" in value:
        import aws_sdk_glue.types.o_auth2_grant_type

        out["OAuth2GrantType"] = (
            aws_sdk_glue.types.o_auth2_grant_type.serialize_aws_json_1_1(
                value["o_auth2_grant_type"]
            )
        )
    if "o_auth2_client_application" in value:
        import aws_sdk_glue.types.o_auth2_client_application

        out["OAuth2ClientApplication"] = (
            aws_sdk_glue.types.o_auth2_client_application.serialize_aws_json_1_1(
                value["o_auth2_client_application"]
            )
        )
    if "token_url" in value:
        out["TokenUrl"] = value["token_url"]
    if "token_url_parameters_map" in value:
        import aws_sdk_glue.types.token_url_parameters_map

        out["TokenUrlParametersMap"] = (
            aws_sdk_glue.types.token_url_parameters_map.serialize_aws_json_1_1(
                value["token_url_parameters_map"]
            )
        )
    if "authorization_code_properties" in value:
        import aws_sdk_glue.types.authorization_code_properties

        out["AuthorizationCodeProperties"] = (
            aws_sdk_glue.types.authorization_code_properties.serialize_aws_json_1_1(
                value["authorization_code_properties"]
            )
        )
    if "o_auth2_credentials" in value:
        import aws_sdk_glue.types.o_auth2_credentials

        out["OAuth2Credentials"] = (
            aws_sdk_glue.types.o_auth2_credentials.serialize_aws_json_1_1(
                value["o_auth2_credentials"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OAuth2PropertiesInput:
    out: OAuth2PropertiesInput = {}  # type: ignore[typeddict-item]
    if "OAuth2GrantType" in data:
        import aws_sdk_glue.types.o_auth2_grant_type

        out["o_auth2_grant_type"] = (
            aws_sdk_glue.types.o_auth2_grant_type.deserialize_aws_json_1_1(
                data["OAuth2GrantType"]
            )
        )
    if "OAuth2ClientApplication" in data:
        import aws_sdk_glue.types.o_auth2_client_application

        out["o_auth2_client_application"] = (
            aws_sdk_glue.types.o_auth2_client_application.deserialize_aws_json_1_1(
                data["OAuth2ClientApplication"]
            )
        )
    if "TokenUrl" in data:
        out["token_url"] = data["TokenUrl"]
    if "TokenUrlParametersMap" in data:
        import aws_sdk_glue.types.token_url_parameters_map

        out["token_url_parameters_map"] = (
            aws_sdk_glue.types.token_url_parameters_map.deserialize_aws_json_1_1(
                data["TokenUrlParametersMap"]
            )
        )
    if "AuthorizationCodeProperties" in data:
        import aws_sdk_glue.types.authorization_code_properties

        out["authorization_code_properties"] = (
            aws_sdk_glue.types.authorization_code_properties.deserialize_aws_json_1_1(
                data["AuthorizationCodeProperties"]
            )
        )
    if "OAuth2Credentials" in data:
        import aws_sdk_glue.types.o_auth2_credentials

        out["o_auth2_credentials"] = (
            aws_sdk_glue.types.o_auth2_credentials.deserialize_aws_json_1_1(
                data["OAuth2Credentials"]
            )
        )
    return out
