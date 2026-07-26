"""Generated from Smithy shape ``com.amazonaws.mediatailor#AdBreakMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediatailor.types.key_value_pair

AdBreakMetadataList: TypeAlias = list[
    "capo_mediatailor.types.key_value_pair.KeyValuePair"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdBreakMetadataList) -> list:
    import capo_mediatailor.types.key_value_pair

    out: list = []
    for item in value:
        out.append(capo_mediatailor.types.key_value_pair.serialize_json(item))
    return out


def deserialize_json(data: list) -> AdBreakMetadataList:
    import capo_mediatailor.types.key_value_pair

    out: AdBreakMetadataList = []
    for item in data:
        out.append(capo_mediatailor.types.key_value_pair.deserialize_json(item))
    return out
