"""Generated from Smithy shape ``com.amazonaws.mediaconvert#InputPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""An input policy allows or disallows a job you submit to run based on the conditions that you specify."""
InputPolicy: TypeAlias = Literal[
    "ALLOWED",
    "DISALLOWED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOWED",
        "DISALLOWED",
    )
)


def serialize_json(value: InputPolicy) -> str:
    return value


def deserialize_json(data: str) -> InputPolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputPolicy value: {data!r}")
    return cast(InputPolicy, data)
