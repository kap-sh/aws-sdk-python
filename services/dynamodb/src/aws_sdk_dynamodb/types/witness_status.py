"""Generated from Smithy shape ``com.amazonaws.dynamodb#WitnessStatus``."""

from typing import Literal, TypeAlias, cast

WitnessStatus: TypeAlias = Literal[
    "CREATING",
    "DELETING",
    "ACTIVE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WitnessStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WitnessStatus:
    return cast(WitnessStatus, data)
