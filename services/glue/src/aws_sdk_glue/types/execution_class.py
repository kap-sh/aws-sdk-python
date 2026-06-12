"""Generated from Smithy shape ``com.amazonaws.glue#ExecutionClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

ExecutionClass: TypeAlias = Literal[
    "FLEX",
    "STANDARD",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FLEX",
        "STANDARD",
    )
)


def serialize_aws_json_1_1(value: ExecutionClass) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionClass:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionClass value: {data!r}")
    return cast(ExecutionClass, data)
