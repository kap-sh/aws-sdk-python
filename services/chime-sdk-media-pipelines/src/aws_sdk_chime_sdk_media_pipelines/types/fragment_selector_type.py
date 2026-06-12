"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#FragmentSelectorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

FragmentSelectorType: TypeAlias = Literal[
    "ProducerTimestamp",
    "ServerTimestamp",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ProducerTimestamp",
        "ServerTimestamp",
    )
)


def serialize_json(value: FragmentSelectorType) -> str:
    return value


def deserialize_json(data: str) -> FragmentSelectorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FragmentSelectorType value: {data!r}")
    return cast(FragmentSelectorType, data)
