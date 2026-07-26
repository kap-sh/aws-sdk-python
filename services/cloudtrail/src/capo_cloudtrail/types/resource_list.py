"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.resource

ResourceList: TypeAlias = list["capo_cloudtrail.types.resource.Resource"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceList) -> list:
    import capo_cloudtrail.types.resource

    out: list = []
    for item in value:
        out.append(capo_cloudtrail.types.resource.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceList:
    import capo_cloudtrail.types.resource

    out: ResourceList = []
    for item in data:
        out.append(capo_cloudtrail.types.resource.deserialize_aws_json_1_1(item))
    return out
