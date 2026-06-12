"""Generated from Smithy shape ``com.amazonaws.clouddirectory#IndexAttachment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.attribute_key_and_value_list
    import aws_sdk_clouddirectory.types.object_identifier


class IndexAttachment(TypedDict):
    indexed_attributes: NotRequired[
        "aws_sdk_clouddirectory.types.attribute_key_and_value_list.AttributeKeyAndValueList"
    ]
    """<p>The indexed attribute values.</p>"""
    object_identifier: NotRequired[
        "aws_sdk_clouddirectory.types.object_identifier.ObjectIdentifier"
    ]
    """<p>In response to <a>ListIndex</a>, the <code>ObjectIdentifier</code> of the object attached to the index. In response to <a>ListAttachedIndices</a>, the <code>ObjectIdentifier</code> of the index attached to the object. This field will always contain the <code>ObjectIdentifier</code> of the object on the opposite side of the attachment specified in the query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IndexAttachment) -> dict:
    out: dict = {}
    if "indexed_attributes" in value:
        import aws_sdk_clouddirectory.types.attribute_key_and_value_list

        out["IndexedAttributes"] = (
            aws_sdk_clouddirectory.types.attribute_key_and_value_list.serialize_json(
                value["indexed_attributes"]
            )
        )
    if "object_identifier" in value:
        out["ObjectIdentifier"] = value["object_identifier"]
    return out


def deserialize_json(data: dict) -> IndexAttachment:
    out: IndexAttachment = {}  # type: ignore[typeddict-item]
    if "IndexedAttributes" in data:
        import aws_sdk_clouddirectory.types.attribute_key_and_value_list

        out["indexed_attributes"] = (
            aws_sdk_clouddirectory.types.attribute_key_and_value_list.deserialize_json(
                data["IndexedAttributes"]
            )
        )
    if "ObjectIdentifier" in data:
        out["object_identifier"] = data["ObjectIdentifier"]
    return out
