"""Generated from Smithy shape ``com.amazonaws.fms#ResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.resource

ResourceList: TypeAlias = list["aws_sdk_fms.types.resource.Resource"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceList) -> list:
    import aws_sdk_fms.types.resource

    out: list = []
    for item in value:
        out.append(aws_sdk_fms.types.resource.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceList:
    import aws_sdk_fms.types.resource

    out: ResourceList = []
    for item in data:
        out.append(aws_sdk_fms.types.resource.deserialize_aws_json_1_1(item))
    return out
