"""Generated from Smithy shape ``com.amazonaws.comprehend#TargetEventTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.event_type_string

TargetEventTypes: TypeAlias = list[
    "capo_comprehend.types.event_type_string.EventTypeString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetEventTypes) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TargetEventTypes:
    return list(data)
