"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#LayoutOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

LayoutOption: TypeAlias = Literal["GridView",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("GridView",))


def serialize_json(value: LayoutOption) -> str:
    return value


def deserialize_json(data: str) -> LayoutOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LayoutOption value: {data!r}")
    return cast(LayoutOption, data)
