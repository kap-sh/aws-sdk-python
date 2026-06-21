"""Generated from Smithy shape ``com.amazonaws.glue#EnableHybridValues``."""

from typing import Literal, TypeAlias, cast

EnableHybridValues: TypeAlias = Literal[
    "TRUE",
    "FALSE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableHybridValues) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EnableHybridValues:
    return cast(EnableHybridValues, data)
