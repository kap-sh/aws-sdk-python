"""Generated from Smithy shape ``com.amazonaws.quicksight#KPISparklineOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.hex_color
    import aws_sdk_quicksight.types.kpi_sparkline_type
    import aws_sdk_quicksight.types.visibility


class KPISparklineOptions(TypedDict):
    visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>The visibility of the sparkline.</p>"""
    type: "aws_sdk_quicksight.types.kpi_sparkline_type.KPISparklineType"
    """<p>The type of the sparkline.</p>"""
    color: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The color of the sparkline.</p>"""
    tooltip_visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>The tooltip visibility of the sparkline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KPISparklineOptions) -> dict:
    out: dict = {}
    if "visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["Visibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    import aws_sdk_quicksight.types.kpi_sparkline_type

    out["Type"] = aws_sdk_quicksight.types.kpi_sparkline_type.serialize_json(
        value["type"]
    )
    if "color" in value:
        out["Color"] = value["color"]
    if "tooltip_visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["TooltipVisibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["tooltip_visibility"]
        )
    return out


def deserialize_json(data: dict) -> KPISparklineOptions:
    out: KPISparklineOptions = {}  # type: ignore[typeddict-item]
    if "Visibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "Type" in data:
        import aws_sdk_quicksight.types.kpi_sparkline_type

        out["type"] = aws_sdk_quicksight.types.kpi_sparkline_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("KPISparklineOptions.type required")
    if "Color" in data:
        out["color"] = data["Color"]
    if "TooltipVisibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["tooltip_visibility"] = (
            aws_sdk_quicksight.types.visibility.deserialize_json(
                data["TooltipVisibility"]
            )
        )
    return out
