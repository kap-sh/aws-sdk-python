"""Generated from Smithy shape ``com.amazonaws.datazone#GlossaryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

GlossaryStatus: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: GlossaryStatus) -> str:
    return value


def deserialize_json(data: str) -> GlossaryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GlossaryStatus value: {data!r}")
    return cast(GlossaryStatus, data)
