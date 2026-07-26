"""Generated from Smithy shape ``com.amazonaws.omics#ShareDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.share_details

ShareDetailsList: TypeAlias = list["capo_omics.types.share_details.ShareDetails"]


# --- restJson1 ser/de ---
def serialize_json(value: ShareDetailsList) -> list:
    import capo_omics.types.share_details

    out: list = []
    for item in value:
        out.append(capo_omics.types.share_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> ShareDetailsList:
    import capo_omics.types.share_details

    out: ShareDetailsList = []
    for item in data:
        out.append(capo_omics.types.share_details.deserialize_json(item))
    return out
