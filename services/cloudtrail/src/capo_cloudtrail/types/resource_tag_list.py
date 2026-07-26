"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ResourceTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.resource_tag

ResourceTagList: TypeAlias = list["capo_cloudtrail.types.resource_tag.ResourceTag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTagList) -> list:
    import capo_cloudtrail.types.resource_tag

    out: list = []
    for item in value:
        out.append(capo_cloudtrail.types.resource_tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceTagList:
    import capo_cloudtrail.types.resource_tag

    out: ResourceTagList = []
    for item in data:
        out.append(capo_cloudtrail.types.resource_tag.deserialize_aws_json_1_1(item))
    return out
