"""Generated from Smithy shape ``com.amazonaws.odb#ResourceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.resource_id

ResourceIdList: TypeAlias = list["capo_odb.types.resource_id.ResourceId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ResourceIdList:
    return list(data)
