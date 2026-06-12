"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ResolutionOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

ResolutionOption: TypeAlias = Literal[
    "HD",
    "FHD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HD",
        "FHD",
    )
)


def serialize_json(value: ResolutionOption) -> str:
    return value


def deserialize_json(data: str) -> ResolutionOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResolutionOption value: {data!r}")
    return cast(ResolutionOption, data)
