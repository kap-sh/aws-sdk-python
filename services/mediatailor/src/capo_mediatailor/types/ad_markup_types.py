"""Generated from Smithy shape ``com.amazonaws.mediatailor#adMarkupTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediatailor.types.ad_markup_type

adMarkupTypes: TypeAlias = list["capo_mediatailor.types.ad_markup_type.AdMarkupType"]


# --- restJson1 ser/de ---
def serialize_json(value: adMarkupTypes) -> list:
    import capo_mediatailor.types.ad_markup_type

    out: list = []
    for item in value:
        out.append(capo_mediatailor.types.ad_markup_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> adMarkupTypes:
    import capo_mediatailor.types.ad_markup_type

    out: adMarkupTypes = []
    for item in data:
        out.append(capo_mediatailor.types.ad_markup_type.deserialize_json(item))
    return out
