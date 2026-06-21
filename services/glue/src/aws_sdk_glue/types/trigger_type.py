"""Generated from Smithy shape ``com.amazonaws.glue#TriggerType``."""

from typing import Literal, TypeAlias, cast

TriggerType: TypeAlias = Literal[
    "SCHEDULED",
    "CONDITIONAL",
    "ON_DEMAND",
    "EVENT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TriggerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TriggerType:
    return cast(TriggerType, data)
