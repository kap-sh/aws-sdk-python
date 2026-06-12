"""Generated from Smithy shape ``com.amazonaws.synthetics#BrowserType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_synthetics.errors import DeserializationError

BrowserType: TypeAlias = Literal[
    "CHROME",
    "FIREFOX",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CHROME",
        "FIREFOX",
    )
)


def serialize_json(value: BrowserType) -> str:
    return value


def deserialize_json(data: str) -> BrowserType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BrowserType value: {data!r}")
    return cast(BrowserType, data)
