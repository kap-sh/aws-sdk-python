"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataGenerationTargetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

MetadataGenerationTargetType: TypeAlias = Literal["ASSET",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ASSET",))


def serialize_json(value: MetadataGenerationTargetType) -> str:
    return value


def deserialize_json(data: str) -> MetadataGenerationTargetType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MetadataGenerationTargetType value: {data!r}"
        )
    return cast(MetadataGenerationTargetType, data)
