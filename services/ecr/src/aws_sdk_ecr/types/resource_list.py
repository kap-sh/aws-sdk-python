"""Generated from Smithy shape ``com.amazonaws.ecr#ResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.resource

ResourceList: TypeAlias = list["aws_sdk_ecr.types.resource.Resource"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceList) -> list:
    import aws_sdk_ecr.types.resource

    out: list = []
    for item in value:
        out.append(aws_sdk_ecr.types.resource.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceList:
    import aws_sdk_ecr.types.resource

    out: ResourceList = []
    for item in data:
        out.append(aws_sdk_ecr.types.resource.deserialize_aws_json_1_1(item))
    return out
