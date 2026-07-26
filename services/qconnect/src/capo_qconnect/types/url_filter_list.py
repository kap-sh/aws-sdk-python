"""Generated from Smithy shape ``com.amazonaws.qconnect#UrlFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.url_filter_pattern

UrlFilterList: TypeAlias = list[
    "capo_qconnect.types.url_filter_pattern.UrlFilterPattern"
]


# --- restJson1 ser/de ---
def serialize_json(value: UrlFilterList) -> list:
    return list(value)


def deserialize_json(data: list) -> UrlFilterList:
    return list(data)
