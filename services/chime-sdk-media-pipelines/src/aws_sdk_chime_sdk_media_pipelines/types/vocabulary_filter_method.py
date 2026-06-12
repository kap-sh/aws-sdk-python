"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#VocabularyFilterMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

VocabularyFilterMethod: TypeAlias = Literal[
    "remove",
    "mask",
    "tag",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "remove",
        "mask",
        "tag",
    )
)


def serialize_json(value: VocabularyFilterMethod) -> str:
    return value


def deserialize_json(data: str) -> VocabularyFilterMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VocabularyFilterMethod value: {data!r}")
    return cast(VocabularyFilterMethod, data)
