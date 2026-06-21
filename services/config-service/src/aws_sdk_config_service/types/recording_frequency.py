"""Generated from Smithy shape ``com.amazonaws.configservice#RecordingFrequency``."""

from typing import Literal, TypeAlias, cast

RecordingFrequency: TypeAlias = Literal[
    "CONTINUOUS",
    "DAILY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordingFrequency) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecordingFrequency:
    return cast(RecordingFrequency, data)
