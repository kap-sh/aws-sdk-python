"""Generated from Smithy shape ``com.amazonaws.appmesh#TagRef``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.tag_key
    import aws_sdk_app_mesh.types.tag_value


class TagRef(TypedDict, closed=True):
    key: "aws_sdk_app_mesh.types.tag_key.TagKey"
    """<p>One part of a key-value pair that make up a tag. A <code>key</code> is a general label that acts like a category for more specific tag values.</p>"""
    value: "aws_sdk_app_mesh.types.tag_value.TagValue"
    """<p>The optional part of a key-value pair that make up a tag. A <code>value</code> acts as a descriptor within a tag category (key).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagRef) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> TagRef:
    out: TagRef = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("TagRef.key required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("TagRef.value required")
    return out
