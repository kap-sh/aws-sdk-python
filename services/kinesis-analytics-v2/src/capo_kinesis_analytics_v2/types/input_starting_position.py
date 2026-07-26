"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#InputStartingPosition``."""

from typing import Literal, TypeAlias, cast

InputStartingPosition: TypeAlias = Literal[
    "NOW",
    "TRIM_HORIZON",
    "LAST_STOPPED_POINT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputStartingPosition) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InputStartingPosition:
    return cast(InputStartingPosition, data)
