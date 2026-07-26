"""Generated from Smithy shape ``com.amazonaws.clouddirectory#TypedLinkAttributeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.attribute_name
    import capo_clouddirectory.types.typed_attribute_value_range


class TypedLinkAttributeRange(TypedDict, closed=True):
    attribute_name: NotRequired[
        "capo_clouddirectory.types.attribute_name.AttributeName"
    ]
    """<p>The unique name of the typed link attribute.</p>"""
    range: (
        "capo_clouddirectory.types.typed_attribute_value_range.TypedAttributeValueRange"
    )
    """<p>The range of attribute values that are being selected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TypedLinkAttributeRange) -> dict:
    out: dict = {}
    if "attribute_name" in value:
        out["AttributeName"] = value["attribute_name"]
    import capo_clouddirectory.types.typed_attribute_value_range

    out["Range"] = capo_clouddirectory.types.typed_attribute_value_range.serialize_json(
        value["range"]
    )
    return out


def deserialize_json(data: dict) -> TypedLinkAttributeRange:
    out: TypedLinkAttributeRange = {}  # type: ignore[typeddict-item]
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    if "Range" in data:
        import capo_clouddirectory.types.typed_attribute_value_range

        out["range"] = (
            capo_clouddirectory.types.typed_attribute_value_range.deserialize_json(
                data["Range"]
            )
        )
    else:
        raise DeserializationError("TypedLinkAttributeRange.range required")
    return out
