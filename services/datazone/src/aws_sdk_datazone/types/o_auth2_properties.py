"""Generated from Smithy shape ``com.amazonaws.datazone#OAuth2Properties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.authorization_code_properties
    import aws_sdk_datazone.types.glue_o_auth2_credentials
    import aws_sdk_datazone.types.o_auth2_client_application
    import aws_sdk_datazone.types.o_auth2_grant_type
    import aws_sdk_datazone.types.token_url_parameters_map


class OAuth2Properties(TypedDict):
    o_auth2_grant_type: NotRequired[
        "aws_sdk_datazone.types.o_auth2_grant_type.OAuth2GrantType"
    ]
    """<p>The OAuth2 grant type of the OAuth2 properties.</p>"""
    o_auth2_client_application: NotRequired[
        "aws_sdk_datazone.types.o_auth2_client_application.OAuth2ClientApplication"
    ]
    """<p>The OAuth2 client application of the OAuth2 properties.</p>"""
    token_url: NotRequired["str"]
    """<p>The OAuth2 token URL of the OAuth2 properties.</p>"""
    token_url_parameters_map: NotRequired[
        "aws_sdk_datazone.types.token_url_parameters_map.TokenUrlParametersMap"
    ]
    """<p>The OAuth2 token URL parameter map of the OAuth2 properties.</p>"""
    authorization_code_properties: NotRequired[
        "aws_sdk_datazone.types.authorization_code_properties.AuthorizationCodeProperties"
    ]
    """<p>The authorization code properties of the OAuth2 properties.</p>"""
    o_auth2_credentials: NotRequired[
        "aws_sdk_datazone.types.glue_o_auth2_credentials.GlueOAuth2Credentials"
    ]
    """<p>The OAuth2 credentials of the OAuth2 properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OAuth2Properties) -> dict:
    out: dict = {}
    if "o_auth2_grant_type" in value:
        import aws_sdk_datazone.types.o_auth2_grant_type

        out["oAuth2GrantType"] = (
            aws_sdk_datazone.types.o_auth2_grant_type.serialize_json(
                value["o_auth2_grant_type"]
            )
        )
    if "o_auth2_client_application" in value:
        import aws_sdk_datazone.types.o_auth2_client_application

        out["oAuth2ClientApplication"] = (
            aws_sdk_datazone.types.o_auth2_client_application.serialize_json(
                value["o_auth2_client_application"]
            )
        )
    if "token_url" in value:
        out["tokenUrl"] = value["token_url"]
    if "token_url_parameters_map" in value:
        import aws_sdk_datazone.types.token_url_parameters_map

        out["tokenUrlParametersMap"] = (
            aws_sdk_datazone.types.token_url_parameters_map.serialize_json(
                value["token_url_parameters_map"]
            )
        )
    if "authorization_code_properties" in value:
        import aws_sdk_datazone.types.authorization_code_properties

        out["authorizationCodeProperties"] = (
            aws_sdk_datazone.types.authorization_code_properties.serialize_json(
                value["authorization_code_properties"]
            )
        )
    if "o_auth2_credentials" in value:
        import aws_sdk_datazone.types.glue_o_auth2_credentials

        out["oAuth2Credentials"] = (
            aws_sdk_datazone.types.glue_o_auth2_credentials.serialize_json(
                value["o_auth2_credentials"]
            )
        )
    return out


def deserialize_json(data: dict) -> OAuth2Properties:
    out: OAuth2Properties = {}  # type: ignore[typeddict-item]
    if "oAuth2GrantType" in data:
        import aws_sdk_datazone.types.o_auth2_grant_type

        out["o_auth2_grant_type"] = (
            aws_sdk_datazone.types.o_auth2_grant_type.deserialize_json(
                data["oAuth2GrantType"]
            )
        )
    if "oAuth2ClientApplication" in data:
        import aws_sdk_datazone.types.o_auth2_client_application

        out["o_auth2_client_application"] = (
            aws_sdk_datazone.types.o_auth2_client_application.deserialize_json(
                data["oAuth2ClientApplication"]
            )
        )
    if "tokenUrl" in data:
        out["token_url"] = data["tokenUrl"]
    if "tokenUrlParametersMap" in data:
        import aws_sdk_datazone.types.token_url_parameters_map

        out["token_url_parameters_map"] = (
            aws_sdk_datazone.types.token_url_parameters_map.deserialize_json(
                data["tokenUrlParametersMap"]
            )
        )
    if "authorizationCodeProperties" in data:
        import aws_sdk_datazone.types.authorization_code_properties

        out["authorization_code_properties"] = (
            aws_sdk_datazone.types.authorization_code_properties.deserialize_json(
                data["authorizationCodeProperties"]
            )
        )
    if "oAuth2Credentials" in data:
        import aws_sdk_datazone.types.glue_o_auth2_credentials

        out["o_auth2_credentials"] = (
            aws_sdk_datazone.types.glue_o_auth2_credentials.deserialize_json(
                data["oAuth2Credentials"]
            )
        )
    return out
