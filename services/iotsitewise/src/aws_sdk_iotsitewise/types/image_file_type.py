"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ImageFileType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

ImageFileType: TypeAlias = Literal["PNG",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PNG",))


def serialize_json(value: ImageFileType) -> str:
    return value


def deserialize_json(data: str) -> ImageFileType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageFileType value: {data!r}")
    return cast(ImageFileType, data)
