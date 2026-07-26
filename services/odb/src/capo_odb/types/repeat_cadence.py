"""Generated from Smithy shape ``com.amazonaws.odb#RepeatCadence``."""

from typing import Literal, TypeAlias, cast

RepeatCadence: TypeAlias = Literal[
    "ONE_TIME",
    "WEEKLY",
    "MONTHLY",
    "YEARLY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RepeatCadence) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RepeatCadence:
    return cast(RepeatCadence, data)
