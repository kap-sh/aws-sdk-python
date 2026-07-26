"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#EmitSystemFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.system_field

EmitSystemFields: TypeAlias = list[
    "capo_cloudwatch_logs.types.system_field.SystemField"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EmitSystemFields) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> EmitSystemFields:
    return list(data)
