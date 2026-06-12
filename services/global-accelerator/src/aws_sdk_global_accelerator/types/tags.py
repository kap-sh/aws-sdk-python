"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.tag

Tags: TypeAlias = list["aws_sdk_global_accelerator.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tags) -> list:
    import aws_sdk_global_accelerator.types.tag

    out: list = []
    for item in value:
        out.append(aws_sdk_global_accelerator.types.tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Tags:
    import aws_sdk_global_accelerator.types.tag

    out: Tags = []
    for item in data:
        out.append(aws_sdk_global_accelerator.types.tag.deserialize_aws_json_1_1(item))
    return out
