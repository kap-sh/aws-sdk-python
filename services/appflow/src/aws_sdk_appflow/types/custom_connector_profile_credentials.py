"""Generated from Smithy shape ``com.amazonaws.appflow#CustomConnectorProfileCredentials``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.api_key_credentials
    import aws_sdk_appflow.types.authentication_type
    import aws_sdk_appflow.types.basic_auth_credentials
    import aws_sdk_appflow.types.custom_auth_credentials
    import aws_sdk_appflow.types.o_auth2_credentials


class CustomConnectorProfileCredentials(TypedDict):
    authentication_type: "aws_sdk_appflow.types.authentication_type.AuthenticationType"
    """<p>The authentication type that the custom connector uses for authenticating while creating a connector profile.</p>"""
    basic: NotRequired[
        "aws_sdk_appflow.types.basic_auth_credentials.BasicAuthCredentials"
    ]
    """<p>The basic credentials that are required for the authentication of the user.</p>"""
    oauth2: NotRequired["aws_sdk_appflow.types.o_auth2_credentials.OAuth2Credentials"]
    """<p>The OAuth 2.0 credentials required for the authentication of the user.</p>"""
    api_key: NotRequired["aws_sdk_appflow.types.api_key_credentials.ApiKeyCredentials"]
    """<p>The API keys required for the authentication of the user.</p>"""
    custom: NotRequired[
        "aws_sdk_appflow.types.custom_auth_credentials.CustomAuthCredentials"
    ]
    """<p>If the connector uses the custom authentication mechanism, this holds the required credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomConnectorProfileCredentials) -> dict:
    out: dict = {}
    import aws_sdk_appflow.types.authentication_type

    out["authenticationType"] = (
        aws_sdk_appflow.types.authentication_type.serialize_json(
            value["authentication_type"]
        )
    )
    if "basic" in value:
        import aws_sdk_appflow.types.basic_auth_credentials

        out["basic"] = aws_sdk_appflow.types.basic_auth_credentials.serialize_json(
            value["basic"]
        )
    if "oauth2" in value:
        import aws_sdk_appflow.types.o_auth2_credentials

        out["oauth2"] = aws_sdk_appflow.types.o_auth2_credentials.serialize_json(
            value["oauth2"]
        )
    if "api_key" in value:
        import aws_sdk_appflow.types.api_key_credentials

        out["apiKey"] = aws_sdk_appflow.types.api_key_credentials.serialize_json(
            value["api_key"]
        )
    if "custom" in value:
        import aws_sdk_appflow.types.custom_auth_credentials

        out["custom"] = aws_sdk_appflow.types.custom_auth_credentials.serialize_json(
            value["custom"]
        )
    return out


def deserialize_json(data: dict) -> CustomConnectorProfileCredentials:
    out: CustomConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if "authenticationType" in data:
        import aws_sdk_appflow.types.authentication_type

        out["authentication_type"] = (
            aws_sdk_appflow.types.authentication_type.deserialize_json(
                data["authenticationType"]
            )
        )
    else:
        raise DeserializationError(
            "CustomConnectorProfileCredentials.authentication_type required"
        )
    if "basic" in data:
        import aws_sdk_appflow.types.basic_auth_credentials

        out["basic"] = aws_sdk_appflow.types.basic_auth_credentials.deserialize_json(
            data["basic"]
        )
    if "oauth2" in data:
        import aws_sdk_appflow.types.o_auth2_credentials

        out["oauth2"] = aws_sdk_appflow.types.o_auth2_credentials.deserialize_json(
            data["oauth2"]
        )
    if "apiKey" in data:
        import aws_sdk_appflow.types.api_key_credentials

        out["api_key"] = aws_sdk_appflow.types.api_key_credentials.deserialize_json(
            data["apiKey"]
        )
    if "custom" in data:
        import aws_sdk_appflow.types.custom_auth_credentials

        out["custom"] = aws_sdk_appflow.types.custom_auth_credentials.deserialize_json(
            data["custom"]
        )
    return out
