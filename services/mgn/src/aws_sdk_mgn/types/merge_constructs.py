"""Generated from Smithy shape ``com.amazonaws.mgn#MergeConstructs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.merge_construct

MergeConstructs: TypeAlias = list["aws_sdk_mgn.types.merge_construct.MergeConstruct"]


# --- restJson1 ser/de ---
def serialize_json(value: MergeConstructs) -> list:
    import aws_sdk_mgn.types.merge_construct

    out: list = []
    for item in value:
        out.append(aws_sdk_mgn.types.merge_construct.serialize_json(item))
    return out


def deserialize_json(data: list) -> MergeConstructs:
    import aws_sdk_mgn.types.merge_construct

    out: MergeConstructs = []
    for item in data:
        out.append(aws_sdk_mgn.types.merge_construct.deserialize_json(item))
    return out
