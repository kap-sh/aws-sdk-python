"""Generated from Smithy shape ``com.amazonaws.glue#Logical``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

Logical: TypeAlias = Literal[
    "AND",
    "ANY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AND",
        "ANY",
    )
)


def serialize_aws_json_1_1(value: Logical) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Logical:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Logical value: {data!r}")
    return cast(Logical, data)
