"""Generated from Smithy shape ``com.amazonaws.quicksight#ReferenceLineValueLabelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.numeric_format_configuration
    import aws_sdk_quicksight.types.reference_line_value_label_relative_position


class ReferenceLineValueLabelConfiguration(TypedDict, closed=True):
    relative_position: NotRequired[
        "aws_sdk_quicksight.types.reference_line_value_label_relative_position.ReferenceLineValueLabelRelativePosition"
    ]
    """<p>The relative position of the value label. Choose one of the following options:</p> <ul> <li> <p> <code>BEFORE_CUSTOM_LABEL</code> </p> </li> <li> <p> <code>AFTER_CUSTOM_LABEL</code> </p> </li> </ul>"""
    format_configuration: NotRequired[
        "aws_sdk_quicksight.types.numeric_format_configuration.NumericFormatConfiguration"
    ]
    """<p>The format configuration of the value label.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceLineValueLabelConfiguration) -> dict:
    out: dict = {}
    if "relative_position" in value:
        import aws_sdk_quicksight.types.reference_line_value_label_relative_position

        out["RelativePosition"] = (
            aws_sdk_quicksight.types.reference_line_value_label_relative_position.serialize_json(
                value["relative_position"]
            )
        )
    if "format_configuration" in value:
        import aws_sdk_quicksight.types.numeric_format_configuration

        out["FormatConfiguration"] = (
            aws_sdk_quicksight.types.numeric_format_configuration.serialize_json(
                value["format_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReferenceLineValueLabelConfiguration:
    out: ReferenceLineValueLabelConfiguration = {}  # type: ignore[typeddict-item]
    if "RelativePosition" in data:
        import aws_sdk_quicksight.types.reference_line_value_label_relative_position

        out["relative_position"] = (
            aws_sdk_quicksight.types.reference_line_value_label_relative_position.deserialize_json(
                data["RelativePosition"]
            )
        )
    if "FormatConfiguration" in data:
        import aws_sdk_quicksight.types.numeric_format_configuration

        out["format_configuration"] = (
            aws_sdk_quicksight.types.numeric_format_configuration.deserialize_json(
                data["FormatConfiguration"]
            )
        )
    return out
