"""Generated from Smithy shape ``com.amazonaws.quicksight#ReferenceLine``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.reference_line_data_configuration
    import aws_sdk_quicksight.types.reference_line_label_configuration
    import aws_sdk_quicksight.types.reference_line_style_configuration
    import aws_sdk_quicksight.types.widget_status


class ReferenceLine(TypedDict):
    status: NotRequired["aws_sdk_quicksight.types.widget_status.WidgetStatus"]
    """<p>The status of the reference line. Choose one of the following options:</p> <ul> <li> <p> <code>ENABLE</code> </p> </li> <li> <p> <code>DISABLE</code> </p> </li> </ul>"""
    data_configuration: "aws_sdk_quicksight.types.reference_line_data_configuration.ReferenceLineDataConfiguration"
    """<p>The data configuration of the reference line.</p>"""
    style_configuration: NotRequired[
        "aws_sdk_quicksight.types.reference_line_style_configuration.ReferenceLineStyleConfiguration"
    ]
    """<p>The style configuration of the reference line.</p>"""
    label_configuration: NotRequired[
        "aws_sdk_quicksight.types.reference_line_label_configuration.ReferenceLineLabelConfiguration"
    ]
    """<p>The label configuration of the reference line.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceLine) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_quicksight.types.widget_status

        out["Status"] = aws_sdk_quicksight.types.widget_status.serialize_json(
            value["status"]
        )
    import aws_sdk_quicksight.types.reference_line_data_configuration

    out["DataConfiguration"] = (
        aws_sdk_quicksight.types.reference_line_data_configuration.serialize_json(
            value["data_configuration"]
        )
    )
    if "style_configuration" in value:
        import aws_sdk_quicksight.types.reference_line_style_configuration

        out["StyleConfiguration"] = (
            aws_sdk_quicksight.types.reference_line_style_configuration.serialize_json(
                value["style_configuration"]
            )
        )
    if "label_configuration" in value:
        import aws_sdk_quicksight.types.reference_line_label_configuration

        out["LabelConfiguration"] = (
            aws_sdk_quicksight.types.reference_line_label_configuration.serialize_json(
                value["label_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReferenceLine:
    out: ReferenceLine = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_quicksight.types.widget_status

        out["status"] = aws_sdk_quicksight.types.widget_status.deserialize_json(
            data["Status"]
        )
    if "DataConfiguration" in data:
        import aws_sdk_quicksight.types.reference_line_data_configuration

        out["data_configuration"] = (
            aws_sdk_quicksight.types.reference_line_data_configuration.deserialize_json(
                data["DataConfiguration"]
            )
        )
    else:
        raise DeserializationError("ReferenceLine.data_configuration required")
    if "StyleConfiguration" in data:
        import aws_sdk_quicksight.types.reference_line_style_configuration

        out["style_configuration"] = (
            aws_sdk_quicksight.types.reference_line_style_configuration.deserialize_json(
                data["StyleConfiguration"]
            )
        )
    if "LabelConfiguration" in data:
        import aws_sdk_quicksight.types.reference_line_label_configuration

        out["label_configuration"] = (
            aws_sdk_quicksight.types.reference_line_label_configuration.deserialize_json(
                data["LabelConfiguration"]
            )
        )
    return out
