"""Generated from Smithy shape ``com.amazonaws.shield#DeleteProtectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_shield.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_shield.types.protection_id


class DeleteProtectionRequest(TypedDict, closed=True):
    protection_id: "aws_sdk_shield.types.protection_id.ProtectionId"
    """<p>The unique identifier (ID) for the <a>Protection</a> object to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteProtectionRequest) -> dict:
    out: dict = {}
    out["ProtectionId"] = value["protection_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteProtectionRequest:
    out: DeleteProtectionRequest = {}  # type: ignore[typeddict-item]
    if "ProtectionId" in data:
        out["protection_id"] = data["ProtectionId"]
    else:
        raise DeserializationError("DeleteProtectionRequest.protection_id required")
    return out
