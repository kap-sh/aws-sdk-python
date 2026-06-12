"""Generated from Smithy shape ``com.amazonaws.identitystore#GroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.resource_id

GroupIds: TypeAlias = list["aws_sdk_identitystore.types.resource_id.ResourceId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> GroupIds:
    return list(data)
