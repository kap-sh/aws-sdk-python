"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#FormatConfigKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video_archived_media.errors import DeserializationError

FormatConfigKey: TypeAlias = Literal["JPEGQuality",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("JPEGQuality",))


def serialize_json(value: FormatConfigKey) -> str:
    return value


def deserialize_json(data: str) -> FormatConfigKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FormatConfigKey value: {data!r}")
    return cast(FormatConfigKey, data)
