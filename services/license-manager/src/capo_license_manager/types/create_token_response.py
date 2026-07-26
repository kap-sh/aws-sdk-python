"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.string
    import capo_license_manager.types.token_string
    import capo_license_manager.types.token_type


class CreateTokenResponse(TypedDict, closed=True):
    token_id: NotRequired["capo_license_manager.types.string.String"]
    """<p>Token ID.</p>"""
    token_type: NotRequired["capo_license_manager.types.token_type.TokenType"]
    """<p>Token type.</p>"""
    token: NotRequired["capo_license_manager.types.token_string.TokenString"]
    """<p>Refresh token, encoded as a JWT token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTokenResponse) -> dict:
    out: dict = {}
    if "token_id" in value:
        out["TokenId"] = value["token_id"]
    if "token_type" in value:
        import capo_license_manager.types.token_type

        out["TokenType"] = capo_license_manager.types.token_type.serialize_aws_json_1_1(
            value["token_type"]
        )
    if "token" in value:
        out["Token"] = value["token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTokenResponse:
    out: CreateTokenResponse = {}  # type: ignore[typeddict-item]
    if "TokenId" in data:
        out["token_id"] = data["TokenId"]
    if "TokenType" in data:
        import capo_license_manager.types.token_type

        out["token_type"] = (
            capo_license_manager.types.token_type.deserialize_aws_json_1_1(
                data["TokenType"]
            )
        )
    if "Token" in data:
        out["token"] = data["Token"]
    return out
