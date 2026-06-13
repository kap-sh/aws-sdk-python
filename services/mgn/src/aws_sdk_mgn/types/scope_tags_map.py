"""Generated from Smithy shape ``com.amazonaws.mgn#ScopeTagsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.scope_tag_key
    import aws_sdk_mgn.types.scope_tag_value

ScopeTagsMap: TypeAlias = dict[
    "aws_sdk_mgn.types.scope_tag_key.ScopeTagKey",
    "aws_sdk_mgn.types.scope_tag_value.ScopeTagValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ScopeTagsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ScopeTagsMap:
    out: ScopeTagsMap = {}
    for key, value in data.items():
        out[key] = value
    return out
