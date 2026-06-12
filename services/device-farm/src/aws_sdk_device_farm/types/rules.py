"""Generated from Smithy shape ``com.amazonaws.devicefarm#Rules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.rule

Rules: TypeAlias = list["aws_sdk_device_farm.types.rule.Rule"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Rules) -> list:
    import aws_sdk_device_farm.types.rule

    out: list = []
    for item in value:
        out.append(aws_sdk_device_farm.types.rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Rules:
    import aws_sdk_device_farm.types.rule

    out: Rules = []
    for item in data:
        out.append(aws_sdk_device_farm.types.rule.deserialize_aws_json_1_1(item))
    return out
