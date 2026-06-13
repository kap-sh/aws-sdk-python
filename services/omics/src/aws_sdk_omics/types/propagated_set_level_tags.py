"""Generated from Smithy shape ``com.amazonaws.omics#PropagatedSetLevelTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.tag_key

PropagatedSetLevelTags: TypeAlias = list["aws_sdk_omics.types.tag_key.TagKey"]


# --- restJson1 ser/de ---
def serialize_json(value: PropagatedSetLevelTags) -> list:
    return list(value)


def deserialize_json(data: list) -> PropagatedSetLevelTags:
    return list(data)
