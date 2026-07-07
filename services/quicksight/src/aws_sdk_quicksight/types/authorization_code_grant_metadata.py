"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthorizationCodeGrantMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.authorization_code_grant_credentials_details
    import aws_sdk_quicksight.types.authorization_code_grant_credentials_source
    import aws_sdk_quicksight.types.endpoint


class AuthorizationCodeGrantMetadata(TypedDict, closed=True):
    base_endpoint: "aws_sdk_quicksight.types.endpoint.Endpoint"
    """<p>The base URL endpoint for the external service.</p>"""
    redirect_url: "aws_sdk_quicksight.types.endpoint.Endpoint"
    """<p>The redirect URL for the OAuth authorization flow.</p>"""
    authorization_code_grant_credentials_source: NotRequired[
        "aws_sdk_quicksight.types.authorization_code_grant_credentials_source.AuthorizationCodeGrantCredentialsSource"
    ]
    """<p>The source of the authorization code grant credentials.</p>"""
    authorization_code_grant_credentials_details: NotRequired[
        "aws_sdk_quicksight.types.authorization_code_grant_credentials_details.AuthorizationCodeGrantCredentialsDetails"
    ]
    """<p>The detailed credentials configuration for authorization code grant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizationCodeGrantMetadata) -> dict:
    out: dict = {}
    out["BaseEndpoint"] = value["base_endpoint"]
    out["RedirectUrl"] = value["redirect_url"]
    if "authorization_code_grant_credentials_source" in value:
        import aws_sdk_quicksight.types.authorization_code_grant_credentials_source

        out["AuthorizationCodeGrantCredentialsSource"] = (
            aws_sdk_quicksight.types.authorization_code_grant_credentials_source.serialize_json(
                value["authorization_code_grant_credentials_source"]
            )
        )
    if "authorization_code_grant_credentials_details" in value:
        import aws_sdk_quicksight.types.authorization_code_grant_credentials_details

        out["AuthorizationCodeGrantCredentialsDetails"] = (
            aws_sdk_quicksight.types.authorization_code_grant_credentials_details.serialize_json(
                value["authorization_code_grant_credentials_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> AuthorizationCodeGrantMetadata:
    out: AuthorizationCodeGrantMetadata = {}  # type: ignore[typeddict-item]
    if "BaseEndpoint" in data:
        out["base_endpoint"] = data["BaseEndpoint"]
    else:
        raise DeserializationError(
            "AuthorizationCodeGrantMetadata.base_endpoint required"
        )
    if "RedirectUrl" in data:
        out["redirect_url"] = data["RedirectUrl"]
    else:
        raise DeserializationError(
            "AuthorizationCodeGrantMetadata.redirect_url required"
        )
    if "AuthorizationCodeGrantCredentialsSource" in data:
        import aws_sdk_quicksight.types.authorization_code_grant_credentials_source

        out["authorization_code_grant_credentials_source"] = (
            aws_sdk_quicksight.types.authorization_code_grant_credentials_source.deserialize_json(
                data["AuthorizationCodeGrantCredentialsSource"]
            )
        )
    if "AuthorizationCodeGrantCredentialsDetails" in data:
        import aws_sdk_quicksight.types.authorization_code_grant_credentials_details

        out["authorization_code_grant_credentials_details"] = (
            aws_sdk_quicksight.types.authorization_code_grant_credentials_details.deserialize_json(
                data["AuthorizationCodeGrantCredentialsDetails"]
            )
        )
    return out
