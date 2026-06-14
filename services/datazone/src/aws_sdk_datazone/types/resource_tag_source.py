"""Generated from Smithy shape ``com.amazonaws.datazone#ResourceTagSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

ResourceTagSource: TypeAlias = Literal[
    "PROJECT",
    "PROJECT_PROFILE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROJECT",
        "PROJECT_PROFILE",
    )
)


def serialize_json(value: ResourceTagSource) -> str:
    return value


def deserialize_json(data: str) -> ResourceTagSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceTagSource value: {data!r}")
    return cast(ResourceTagSource, data)
