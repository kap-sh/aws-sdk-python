"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ScteFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.scte_filter

ScteFilterList: TypeAlias = list["capo_mediapackagev2.types.scte_filter.ScteFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: ScteFilterList) -> list:
    import capo_mediapackagev2.types.scte_filter

    out: list = []
    for item in value:
        out.append(capo_mediapackagev2.types.scte_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScteFilterList:
    import capo_mediapackagev2.types.scte_filter

    out: ScteFilterList = []
    for item in data:
        out.append(capo_mediapackagev2.types.scte_filter.deserialize_json(item))
    return out
