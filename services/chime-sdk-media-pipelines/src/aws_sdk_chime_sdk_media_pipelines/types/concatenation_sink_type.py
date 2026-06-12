"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ConcatenationSinkType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

ConcatenationSinkType: TypeAlias = Literal["S3Bucket",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("S3Bucket",))


def serialize_json(value: ConcatenationSinkType) -> str:
    return value


def deserialize_json(data: str) -> ConcatenationSinkType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConcatenationSinkType value: {data!r}")
    return cast(ConcatenationSinkType, data)
