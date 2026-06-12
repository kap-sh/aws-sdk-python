"""Generated from Smithy shape ``com.amazonaws.securityhub#RegisterConnectorV2Request``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class RegisterConnectorV2Request(TypedDict):
    auth_code: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The authCode retrieved from authUrl to complete the OAuth 2.0 authorization code flow.</p>"""
    auth_state: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The authState retrieved from authUrl to complete the OAuth 2.0 authorization code flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterConnectorV2Request) -> dict:
    out: dict = {}
    if "auth_code" in value:
        out["AuthCode"] = value["auth_code"]
    if "auth_state" in value:
        out["AuthState"] = value["auth_state"]
    return out


def deserialize_json(data: dict) -> RegisterConnectorV2Request:
    out: RegisterConnectorV2Request = {}  # type: ignore[typeddict-item]
    if "AuthCode" in data:
        out["auth_code"] = data["AuthCode"]
    if "AuthState" in data:
        out["auth_state"] = data["AuthState"]
    return out
