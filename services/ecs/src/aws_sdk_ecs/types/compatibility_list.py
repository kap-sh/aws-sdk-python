"""Generated from Smithy shape ``com.amazonaws.ecs#CompatibilityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.compatibility

CompatibilityList: TypeAlias = list["aws_sdk_ecs.types.compatibility.Compatibility"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompatibilityList) -> list:
    import aws_sdk_ecs.types.compatibility

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.compatibility.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CompatibilityList:
    import aws_sdk_ecs.types.compatibility

    out: CompatibilityList = []
    for item in data:
        out.append(aws_sdk_ecs.types.compatibility.deserialize_aws_json_1_1(item))
    return out
