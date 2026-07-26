"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfLFTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dataexchange.types.lf_tag

ListOfLFTags: TypeAlias = list["capo_dataexchange.types.lf_tag.LFTag"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfLFTags) -> list:
    import capo_dataexchange.types.lf_tag

    out: list = []
    for item in value:
        out.append(capo_dataexchange.types.lf_tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfLFTags:
    import capo_dataexchange.types.lf_tag

    out: ListOfLFTags = []
    for item in data:
        out.append(capo_dataexchange.types.lf_tag.deserialize_json(item))
    return out
