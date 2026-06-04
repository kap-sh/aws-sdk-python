"""Generated from Smithy shape ``com.amazonaws.ecs#Settings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.setting

Settings: TypeAlias = list["aws_sdk_ecs.types.setting.Setting"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Settings) -> list:
    import aws_sdk_ecs.types.setting

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.setting.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Settings:
    import aws_sdk_ecs.types.setting

    out: Settings = []
    for item in data:
        out.append(aws_sdk_ecs.types.setting.deserialize_aws_json_1_1(item))
    return out
