"""Generated from Smithy shape ``com.amazonaws.shield#DeleteProtectionGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_shield.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_shield.types.protection_group_id


class DeleteProtectionGroupRequest(TypedDict):
    protection_group_id: "aws_sdk_shield.types.protection_group_id.ProtectionGroupId"
    """<p>The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteProtectionGroupRequest) -> dict:
    out: dict = {}
    out["ProtectionGroupId"] = value["protection_group_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteProtectionGroupRequest:
    out: DeleteProtectionGroupRequest = {}  # type: ignore[typeddict-item]
    if "ProtectionGroupId" in data:
        out["protection_group_id"] = data["ProtectionGroupId"]
    else:
        raise DeserializationError(
            "DeleteProtectionGroupRequest.protection_group_id required"
        )
    return out
