"""Generated from Smithy shape ``com.amazonaws.firehose#Connectivity``."""

from typing import Literal, TypeAlias, cast

Connectivity: TypeAlias = Literal[
    "PUBLIC",
    "PRIVATE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Connectivity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Connectivity:
    return cast(Connectivity, data)
