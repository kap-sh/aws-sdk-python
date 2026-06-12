"""Generated from Smithy shape ``com.amazonaws.clouddirectory#TypedLinkAttributeRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.attribute_name
    import aws_sdk_clouddirectory.types.typed_attribute_value_range


class TypedLinkAttributeRange(TypedDict):
    attribute_name: NotRequired[
        "aws_sdk_clouddirectory.types.attribute_name.AttributeName"
    ]
    """<p>The unique name of the typed link attribute.</p>"""
    range: "aws_sdk_clouddirectory.types.typed_attribute_value_range.TypedAttributeValueRange"
    """<p>The range of attribute values that are being selected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TypedLinkAttributeRange) -> dict:
    out: dict = {}
    if "attribute_name" in value:
        out["AttributeName"] = value["attribute_name"]
    import aws_sdk_clouddirectory.types.typed_attribute_value_range

    out["Range"] = (
        aws_sdk_clouddirectory.types.typed_attribute_value_range.serialize_json(
            value["range"]
        )
    )
    return out


def deserialize_json(data: dict) -> TypedLinkAttributeRange:
    out: TypedLinkAttributeRange = {}  # type: ignore[typeddict-item]
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    if "Range" in data:
        import aws_sdk_clouddirectory.types.typed_attribute_value_range

        out["range"] = (
            aws_sdk_clouddirectory.types.typed_attribute_value_range.deserialize_json(
                data["Range"]
            )
        )
    else:
        raise DeserializationError("TypedLinkAttributeRange.range required")
    return out
