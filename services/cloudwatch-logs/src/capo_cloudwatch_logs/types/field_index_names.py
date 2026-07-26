"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#FieldIndexNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.field_index_name

FieldIndexNames: TypeAlias = list[
    "capo_cloudwatch_logs.types.field_index_name.FieldIndexName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FieldIndexNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FieldIndexNames:
    return list(data)
