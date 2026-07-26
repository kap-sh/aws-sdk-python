"""Generated from Smithy shape ``com.amazonaws.lightsail#SetupStatus``."""

from typing import Literal, TypeAlias, cast

SetupStatus: TypeAlias = Literal[
    "succeeded",
    "failed",
    "inProgress",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetupStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SetupStatus:
    return cast(SetupStatus, data)
