"""Generated from Smithy shape ``com.amazonaws.frauddetector#EventIngestion``."""

from typing import Literal, TypeAlias, cast

EventIngestion: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventIngestion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventIngestion:
    return cast(EventIngestion, data)
