"""Generated from Smithy shape ``com.amazonaws.glue#SessionType``."""

from typing import Literal, TypeAlias, cast

SessionType: TypeAlias = Literal[
    "LIVY",
    "SPARK_CONNECT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SessionType:
    return cast(SessionType, data)
