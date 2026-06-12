"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfLFTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.lf_tag

ListOfLFTags: TypeAlias = list["aws_sdk_dataexchange.types.lf_tag.LFTag"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfLFTags) -> list:
    import aws_sdk_dataexchange.types.lf_tag

    out: list = []
    for item in value:
        out.append(aws_sdk_dataexchange.types.lf_tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfLFTags:
    import aws_sdk_dataexchange.types.lf_tag

    out: ListOfLFTags = []
    for item in data:
        out.append(aws_sdk_dataexchange.types.lf_tag.deserialize_json(item))
    return out
