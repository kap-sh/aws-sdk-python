"""Generated from Smithy shape ``com.amazonaws.devicefarm#NetworkProfileType``."""

from typing import Literal, TypeAlias, cast

NetworkProfileType: TypeAlias = Literal[
    "CURATED",
    "PRIVATE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkProfileType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NetworkProfileType:
    return cast(NetworkProfileType, data)
