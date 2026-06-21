"""Generated from Smithy shape ``com.amazonaws.kms#RotationType``."""

from typing import Literal, TypeAlias, cast

RotationType: TypeAlias = Literal[
    "AUTOMATIC",
    "ON_DEMAND",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RotationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RotationType:
    return cast(RotationType, data)
