"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ConcatenationSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

ConcatenationSourceType: TypeAlias = Literal["MediaCapturePipeline",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MediaCapturePipeline",))


def serialize_json(value: ConcatenationSourceType) -> str:
    return value


def deserialize_json(data: str) -> ConcatenationSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConcatenationSourceType value: {data!r}")
    return cast(ConcatenationSourceType, data)
