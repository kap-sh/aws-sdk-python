"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationMode``."""

from typing import Literal, TypeAlias, cast

ApplicationMode: TypeAlias = Literal[
    "STREAMING",
    "INTERACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApplicationMode:
    return cast(ApplicationMode, data)
