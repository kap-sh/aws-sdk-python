"""Generated from Smithy shape ``com.amazonaws.cloudtrail#MaxEventSize``."""

from typing import Literal, TypeAlias, cast

MaxEventSize: TypeAlias = Literal[
    "Standard",
    "Large",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaxEventSize) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MaxEventSize:
    return cast(MaxEventSize, data)
