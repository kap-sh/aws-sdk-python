"""Generated from Smithy shape ``com.amazonaws.quicksight#ReferenceLineLabelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.font_configuration
    import aws_sdk_quicksight.types.hex_color
    import aws_sdk_quicksight.types.reference_line_custom_label_configuration
    import aws_sdk_quicksight.types.reference_line_label_horizontal_position
    import aws_sdk_quicksight.types.reference_line_label_vertical_position
    import aws_sdk_quicksight.types.reference_line_value_label_configuration


class ReferenceLineLabelConfiguration(TypedDict, closed=True):
    value_label_configuration: NotRequired[
        "aws_sdk_quicksight.types.reference_line_value_label_configuration.ReferenceLineValueLabelConfiguration"
    ]
    """<p>The value label configuration of the label in a reference line.</p>"""
    custom_label_configuration: NotRequired[
        "aws_sdk_quicksight.types.reference_line_custom_label_configuration.ReferenceLineCustomLabelConfiguration"
    ]
    """<p>The custom label configuration of the label in a reference line.</p>"""
    font_configuration: NotRequired[
        "aws_sdk_quicksight.types.font_configuration.FontConfiguration"
    ]
    """<p>The font configuration of the label in a reference line.</p>"""
    font_color: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The font color configuration of the label in a reference line.</p>"""
    horizontal_position: NotRequired[
        "aws_sdk_quicksight.types.reference_line_label_horizontal_position.ReferenceLineLabelHorizontalPosition"
    ]
    """<p>The horizontal position configuration of the label in a reference line. Choose one of the following options:</p> <ul> <li> <p> <code>LEFT</code> </p> </li> <li> <p> <code>CENTER</code> </p> </li> <li> <p> <code>RIGHT</code> </p> </li> </ul>"""
    vertical_position: NotRequired[
        "aws_sdk_quicksight.types.reference_line_label_vertical_position.ReferenceLineLabelVerticalPosition"
    ]
    """<p>The vertical position configuration of the label in a reference line. Choose one of the following options:</p> <ul> <li> <p> <code>ABOVE</code> </p> </li> <li> <p> <code>BELOW</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceLineLabelConfiguration) -> dict:
    out: dict = {}
    if "value_label_configuration" in value:
        import aws_sdk_quicksight.types.reference_line_value_label_configuration

        out["ValueLabelConfiguration"] = (
            aws_sdk_quicksight.types.reference_line_value_label_configuration.serialize_json(
                value["value_label_configuration"]
            )
        )
    if "custom_label_configuration" in value:
        import aws_sdk_quicksight.types.reference_line_custom_label_configuration

        out["CustomLabelConfiguration"] = (
            aws_sdk_quicksight.types.reference_line_custom_label_configuration.serialize_json(
                value["custom_label_configuration"]
            )
        )
    if "font_configuration" in value:
        import aws_sdk_quicksight.types.font_configuration

        out["FontConfiguration"] = (
            aws_sdk_quicksight.types.font_configuration.serialize_json(
                value["font_configuration"]
            )
        )
    if "font_color" in value:
        out["FontColor"] = value["font_color"]
    if "horizontal_position" in value:
        import aws_sdk_quicksight.types.reference_line_label_horizontal_position

        out["HorizontalPosition"] = (
            aws_sdk_quicksight.types.reference_line_label_horizontal_position.serialize_json(
                value["horizontal_position"]
            )
        )
    if "vertical_position" in value:
        import aws_sdk_quicksight.types.reference_line_label_vertical_position

        out["VerticalPosition"] = (
            aws_sdk_quicksight.types.reference_line_label_vertical_position.serialize_json(
                value["vertical_position"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReferenceLineLabelConfiguration:
    out: ReferenceLineLabelConfiguration = {}  # type: ignore[typeddict-item]
    if "ValueLabelConfiguration" in data:
        import aws_sdk_quicksight.types.reference_line_value_label_configuration

        out["value_label_configuration"] = (
            aws_sdk_quicksight.types.reference_line_value_label_configuration.deserialize_json(
                data["ValueLabelConfiguration"]
            )
        )
    if "CustomLabelConfiguration" in data:
        import aws_sdk_quicksight.types.reference_line_custom_label_configuration

        out["custom_label_configuration"] = (
            aws_sdk_quicksight.types.reference_line_custom_label_configuration.deserialize_json(
                data["CustomLabelConfiguration"]
            )
        )
    if "FontConfiguration" in data:
        import aws_sdk_quicksight.types.font_configuration

        out["font_configuration"] = (
            aws_sdk_quicksight.types.font_configuration.deserialize_json(
                data["FontConfiguration"]
            )
        )
    if "FontColor" in data:
        out["font_color"] = data["FontColor"]
    if "HorizontalPosition" in data:
        import aws_sdk_quicksight.types.reference_line_label_horizontal_position

        out["horizontal_position"] = (
            aws_sdk_quicksight.types.reference_line_label_horizontal_position.deserialize_json(
                data["HorizontalPosition"]
            )
        )
    if "VerticalPosition" in data:
        import aws_sdk_quicksight.types.reference_line_label_vertical_position

        out["vertical_position"] = (
            aws_sdk_quicksight.types.reference_line_label_vertical_position.deserialize_json(
                data["VerticalPosition"]
            )
        )
    return out
