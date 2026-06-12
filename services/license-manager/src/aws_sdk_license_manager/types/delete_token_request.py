"""Generated from Smithy shape ``com.amazonaws.licensemanager#DeleteTokenRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.string


class DeleteTokenRequest(TypedDict):
    token_id: "aws_sdk_license_manager.types.string.String"
    """<p>Token ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTokenRequest) -> dict:
    out: dict = {}
    out["TokenId"] = value["token_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTokenRequest:
    out: DeleteTokenRequest = {}  # type: ignore[typeddict-item]
    if "TokenId" in data:
        out["token_id"] = data["TokenId"]
    else:
        raise DeserializationError("DeleteTokenRequest.token_id required")
    return out
