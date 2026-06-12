"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateTokenResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.string
    import aws_sdk_license_manager.types.token_string
    import aws_sdk_license_manager.types.token_type


class CreateTokenResponse(TypedDict):
    token_id: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Token ID.</p>"""
    token_type: NotRequired["aws_sdk_license_manager.types.token_type.TokenType"]
    """<p>Token type.</p>"""
    token: NotRequired["aws_sdk_license_manager.types.token_string.TokenString"]
    """<p>Refresh token, encoded as a JWT token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTokenResponse) -> dict:
    out: dict = {}
    if "token_id" in value:
        out["TokenId"] = value["token_id"]
    if "token_type" in value:
        import aws_sdk_license_manager.types.token_type

        out["TokenType"] = (
            aws_sdk_license_manager.types.token_type.serialize_aws_json_1_1(
                value["token_type"]
            )
        )
    if "token" in value:
        out["Token"] = value["token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTokenResponse:
    out: CreateTokenResponse = {}  # type: ignore[typeddict-item]
    if "TokenId" in data:
        out["token_id"] = data["TokenId"]
    if "TokenType" in data:
        import aws_sdk_license_manager.types.token_type

        out["token_type"] = (
            aws_sdk_license_manager.types.token_type.deserialize_aws_json_1_1(
                data["TokenType"]
            )
        )
    if "Token" in data:
        out["token"] = data["Token"]
    return out
