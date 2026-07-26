"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ObjectAttributeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.attribute_key
    import capo_clouddirectory.types.typed_attribute_value_range


class ObjectAttributeRange(TypedDict, closed=True):
    attribute_key: NotRequired["capo_clouddirectory.types.attribute_key.AttributeKey"]
    """<p>The key of the attribute that the attribute range covers.</p>"""
    range: NotRequired[
        "capo_clouddirectory.types.typed_attribute_value_range.TypedAttributeValueRange"
    ]
    """<p>The range of attribute values being selected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ObjectAttributeRange) -> dict:
    out: dict = {}
    if "attribute_key" in value:
        import capo_clouddirectory.types.attribute_key

        out["AttributeKey"] = capo_clouddirectory.types.attribute_key.serialize_json(
            value["attribute_key"]
        )
    if "range" in value:
        import capo_clouddirectory.types.typed_attribute_value_range

        out["Range"] = (
            capo_clouddirectory.types.typed_attribute_value_range.serialize_json(
                value["range"]
            )
        )
    return out


def deserialize_json(data: dict) -> ObjectAttributeRange:
    out: ObjectAttributeRange = {}  # type: ignore[typeddict-item]
    if "AttributeKey" in data:
        import capo_clouddirectory.types.attribute_key

        out["attribute_key"] = capo_clouddirectory.types.attribute_key.deserialize_json(
            data["AttributeKey"]
        )
    if "Range" in data:
        import capo_clouddirectory.types.typed_attribute_value_range

        out["range"] = (
            capo_clouddirectory.types.typed_attribute_value_range.deserialize_json(
                data["Range"]
            )
        )
    return out
