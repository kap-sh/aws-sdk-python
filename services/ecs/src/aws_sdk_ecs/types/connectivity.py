"""Generated from Smithy shape ``com.amazonaws.ecs#Connectivity``."""

from typing import Literal, TypeAlias, cast

Connectivity: TypeAlias = Literal[
    "CONNECTED",
    "DISCONNECTED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Connectivity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Connectivity:
    return cast(Connectivity, data)
