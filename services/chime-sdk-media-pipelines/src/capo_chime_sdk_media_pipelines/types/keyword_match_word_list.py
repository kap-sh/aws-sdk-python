"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#KeywordMatchWordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.keyword

KeywordMatchWordList: TypeAlias = list[
    "capo_chime_sdk_media_pipelines.types.keyword.Keyword"
]


# --- restJson1 ser/de ---
def serialize_json(value: KeywordMatchWordList) -> list:
    return list(value)


def deserialize_json(data: list) -> KeywordMatchWordList:
    return list(data)
