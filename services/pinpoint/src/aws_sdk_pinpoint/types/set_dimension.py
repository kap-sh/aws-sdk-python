"""Generated from Smithy shape ``com.amazonaws.pinpoint#SetDimension``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.dimension_type
    import aws_sdk_pinpoint.types.list_of__string


class SetDimension(TypedDict):
    dimension_type: NotRequired["aws_sdk_pinpoint.types.dimension_type.DimensionType"]
    """<p>The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.</p>"""
    values: NotRequired["aws_sdk_pinpoint.types.list_of__string.ListOf__string"]
    """<p>The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetDimension) -> dict:
    out: dict = {}
    if "dimension_type" in value:
        import aws_sdk_pinpoint.types.dimension_type

        out["DimensionType"] = aws_sdk_pinpoint.types.dimension_type.serialize_json(
            value["dimension_type"]
        )
    if "values" in value:
        import aws_sdk_pinpoint.types.list_of__string

        out["Values"] = aws_sdk_pinpoint.types.list_of__string.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> SetDimension:
    out: SetDimension = {}  # type: ignore[typeddict-item]
    if "DimensionType" in data:
        import aws_sdk_pinpoint.types.dimension_type

        out["dimension_type"] = aws_sdk_pinpoint.types.dimension_type.deserialize_json(
            data["DimensionType"]
        )
    if "Values" in data:
        import aws_sdk_pinpoint.types.list_of__string

        out["values"] = aws_sdk_pinpoint.types.list_of__string.deserialize_json(
            data["Values"]
        )
    return out
