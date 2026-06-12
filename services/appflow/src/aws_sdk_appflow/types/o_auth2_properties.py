"""Generated from Smithy shape ``com.amazonaws.appflow#OAuth2Properties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.o_auth2_grant_type
    import aws_sdk_appflow.types.token_url
    import aws_sdk_appflow.types.token_url_custom_properties


class OAuth2Properties(TypedDict):
    token_url: "aws_sdk_appflow.types.token_url.TokenUrl"
    """<p>The token URL required for OAuth 2.0 authentication.</p>"""
    o_auth2_grant_type: "aws_sdk_appflow.types.o_auth2_grant_type.OAuth2GrantType"
    """<p>The OAuth 2.0 grant type used by connector for OAuth 2.0 authentication.</p>"""
    token_url_custom_properties: NotRequired[
        "aws_sdk_appflow.types.token_url_custom_properties.TokenUrlCustomProperties"
    ]
    """<p>Associates your token URL with a map of properties that you define. Use this parameter to provide any additional details that the connector requires to authenticate your request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OAuth2Properties) -> dict:
    out: dict = {}
    out["tokenUrl"] = value["token_url"]
    import aws_sdk_appflow.types.o_auth2_grant_type

    out["oAuth2GrantType"] = aws_sdk_appflow.types.o_auth2_grant_type.serialize_json(
        value["o_auth2_grant_type"]
    )
    if "token_url_custom_properties" in value:
        import aws_sdk_appflow.types.token_url_custom_properties

        out["tokenUrlCustomProperties"] = (
            aws_sdk_appflow.types.token_url_custom_properties.serialize_json(
                value["token_url_custom_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> OAuth2Properties:
    out: OAuth2Properties = {}  # type: ignore[typeddict-item]
    if "tokenUrl" in data:
        out["token_url"] = data["tokenUrl"]
    else:
        raise DeserializationError("OAuth2Properties.token_url required")
    if "oAuth2GrantType" in data:
        import aws_sdk_appflow.types.o_auth2_grant_type

        out["o_auth2_grant_type"] = (
            aws_sdk_appflow.types.o_auth2_grant_type.deserialize_json(
                data["oAuth2GrantType"]
            )
        )
    else:
        raise DeserializationError("OAuth2Properties.o_auth2_grant_type required")
    if "tokenUrlCustomProperties" in data:
        import aws_sdk_appflow.types.token_url_custom_properties

        out["token_url_custom_properties"] = (
            aws_sdk_appflow.types.token_url_custom_properties.deserialize_json(
                data["tokenUrlCustomProperties"]
            )
        )
    return out
