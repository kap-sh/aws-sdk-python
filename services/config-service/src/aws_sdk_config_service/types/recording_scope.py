"""Generated from Smithy shape ``com.amazonaws.configservice#RecordingScope``."""

from typing import Literal, TypeAlias, cast

RecordingScope: TypeAlias = Literal[
    "INTERNAL",
    "PAID",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordingScope) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecordingScope:
    return cast(RecordingScope, data)
