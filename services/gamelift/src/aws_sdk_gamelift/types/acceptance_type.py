"""Generated from Smithy shape ``com.amazonaws.gamelift#AcceptanceType``."""

from typing import Literal, TypeAlias, cast

AcceptanceType: TypeAlias = Literal[
    "ACCEPT",
    "REJECT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceptanceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AcceptanceType:
    return cast(AcceptanceType, data)
