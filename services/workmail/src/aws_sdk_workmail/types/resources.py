"""Generated from Smithy shape ``com.amazonaws.workmail#Resources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workmail.types.resource

Resources: TypeAlias = list["aws_sdk_workmail.types.resource.Resource"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Resources) -> list:
    import aws_sdk_workmail.types.resource

    out: list = []
    for item in value:
        out.append(aws_sdk_workmail.types.resource.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Resources:
    import aws_sdk_workmail.types.resource

    out: Resources = []
    for item in data:
        out.append(aws_sdk_workmail.types.resource.deserialize_aws_json_1_1(item))
    return out
