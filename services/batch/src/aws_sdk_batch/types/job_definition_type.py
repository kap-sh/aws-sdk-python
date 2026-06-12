"""Generated from Smithy shape ``com.amazonaws.batch#JobDefinitionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

JobDefinitionType: TypeAlias = Literal[
    "container",
    "multinode",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "container",
        "multinode",
    )
)


def serialize_json(value: JobDefinitionType) -> str:
    return value


def deserialize_json(data: str) -> JobDefinitionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobDefinitionType value: {data!r}")
    return cast(JobDefinitionType, data)
