"""Generated from Smithy shape ``com.amazonaws.glue#EnableHybridValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

EnableHybridValues: TypeAlias = Literal[
    "TRUE",
    "FALSE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRUE",
        "FALSE",
    )
)


def serialize_aws_json_1_1(value: EnableHybridValues) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EnableHybridValues:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EnableHybridValues value: {data!r}")
    return cast(EnableHybridValues, data)
