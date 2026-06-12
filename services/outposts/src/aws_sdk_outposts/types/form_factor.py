"""Generated from Smithy shape ``com.amazonaws.outposts#FormFactor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

FormFactor: TypeAlias = Literal[
    "RACK",
    "SERVER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RACK",
        "SERVER",
    )
)


def serialize_json(value: FormFactor) -> str:
    return value


def deserialize_json(data: str) -> FormFactor:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FormFactor value: {data!r}")
    return cast(FormFactor, data)
