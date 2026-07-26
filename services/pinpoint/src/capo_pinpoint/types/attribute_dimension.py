"""Generated from Smithy shape ``com.amazonaws.pinpoint#AttributeDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.attribute_type
    import capo_pinpoint.types.list_of__string


class AttributeDimension(TypedDict, closed=True):
    attribute_type: NotRequired["capo_pinpoint.types.attribute_type.AttributeType"]
    """<p>The type of segment dimension to use. Valid values are: <ul><li>INCLUSIVE - endpoints that have attributes matching the values are included in the segment.</li><li>EXCLUSIVE - endpoints that have attributes matching the values are excluded in the segment.</li><li>CONTAINS - endpoints that have attributes' substrings match the values are included in the segment.</li><li>BEFORE - endpoints with attributes read as ISO_INSTANT datetimes before the value are included in the segment.</li><li>AFTER - endpoints with attributes read as ISO_INSTANT datetimes after the value are included in the segment.</li><li>ON - endpoints with attributes read as ISO_INSTANT dates on the value are included in the segment. Time is ignored in this comparison.</li><li>BETWEEN - endpoints with attributes read as ISO_INSTANT datetimes between the values are included in the segment.</li></p>"""
    values: NotRequired["capo_pinpoint.types.list_of__string.ListOf__string"]
    """<p>The criteria values to use for the segment dimension. Depending on the value of the AttributeType property, endpoints are included or excluded from the segment if their attribute values match the criteria values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeDimension) -> dict:
    out: dict = {}
    if "attribute_type" in value:
        import capo_pinpoint.types.attribute_type

        out["AttributeType"] = capo_pinpoint.types.attribute_type.serialize_json(
            value["attribute_type"]
        )
    if "values" in value:
        import capo_pinpoint.types.list_of__string

        out["Values"] = capo_pinpoint.types.list_of__string.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> AttributeDimension:
    out: AttributeDimension = {}  # type: ignore[typeddict-item]
    if "AttributeType" in data:
        import capo_pinpoint.types.attribute_type

        out["attribute_type"] = capo_pinpoint.types.attribute_type.deserialize_json(
            data["AttributeType"]
        )
    if "Values" in data:
        import capo_pinpoint.types.list_of__string

        out["values"] = capo_pinpoint.types.list_of__string.deserialize_json(
            data["Values"]
        )
    return out
