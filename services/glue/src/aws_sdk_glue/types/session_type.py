"""Generated from Smithy shape ``com.amazonaws.glue#SessionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

SessionType: TypeAlias = Literal[
    "LIVY",
    "SPARK_CONNECT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LIVY",
        "SPARK_CONNECT",
    )
)


def serialize_aws_json_1_1(value: SessionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SessionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SessionType value: {data!r}")
    return cast(SessionType, data)
