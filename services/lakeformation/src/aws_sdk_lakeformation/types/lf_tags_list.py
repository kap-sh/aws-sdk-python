"""Generated from Smithy shape ``com.amazonaws.lakeformation#LFTagsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.lf_tag_pair

LFTagsList: TypeAlias = list["aws_sdk_lakeformation.types.lf_tag_pair.LFTagPair"]


# --- restJson1 ser/de ---
def serialize_json(value: LFTagsList) -> list:
    import aws_sdk_lakeformation.types.lf_tag_pair

    out: list = []
    for item in value:
        out.append(aws_sdk_lakeformation.types.lf_tag_pair.serialize_json(item))
    return out


def deserialize_json(data: list) -> LFTagsList:
    import aws_sdk_lakeformation.types.lf_tag_pair

    out: LFTagsList = []
    for item in data:
        out.append(aws_sdk_lakeformation.types.lf_tag_pair.deserialize_json(item))
    return out
