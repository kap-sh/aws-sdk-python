"""Generated from Smithy shape ``com.amazonaws.quicksight#DataLabelOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_label_content
    import aws_sdk_quicksight.types.data_label_overlap
    import aws_sdk_quicksight.types.data_label_position
    import aws_sdk_quicksight.types.data_label_types
    import aws_sdk_quicksight.types.font_configuration
    import aws_sdk_quicksight.types.hex_color
    import aws_sdk_quicksight.types.visibility


class DataLabelOptions(TypedDict):
    visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>Determines the visibility of the data labels.</p>"""
    category_label_visibility: NotRequired[
        "aws_sdk_quicksight.types.visibility.Visibility"
    ]
    """<p>Determines the visibility of the category field labels.</p>"""
    measure_label_visibility: NotRequired[
        "aws_sdk_quicksight.types.visibility.Visibility"
    ]
    """<p>Determines the visibility of the measure field labels.</p>"""
    data_label_types: NotRequired[
        "aws_sdk_quicksight.types.data_label_types.DataLabelTypes"
    ]
    """<p>The option that determines the data label type.</p>"""
    position: NotRequired[
        "aws_sdk_quicksight.types.data_label_position.DataLabelPosition"
    ]
    """<p>Determines the position of the data labels.</p>"""
    label_content: NotRequired[
        "aws_sdk_quicksight.types.data_label_content.DataLabelContent"
    ]
    """<p>Determines the content of the data labels.</p>"""
    label_font_configuration: NotRequired[
        "aws_sdk_quicksight.types.font_configuration.FontConfiguration"
    ]
    """<p>Determines the font configuration of the data labels.</p>"""
    label_color: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>Determines the color of the data labels.</p>"""
    overlap: NotRequired["aws_sdk_quicksight.types.data_label_overlap.DataLabelOverlap"]
    """<p>Determines whether overlap is enabled or disabled for the data labels.</p>"""
    totals_visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>Determines the visibility of the total.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLabelOptions) -> dict:
    out: dict = {}
    if "visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["Visibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "category_label_visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["CategoryLabelVisibility"] = (
            aws_sdk_quicksight.types.visibility.serialize_json(
                value["category_label_visibility"]
            )
        )
    if "measure_label_visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["MeasureLabelVisibility"] = (
            aws_sdk_quicksight.types.visibility.serialize_json(
                value["measure_label_visibility"]
            )
        )
    if "data_label_types" in value:
        import aws_sdk_quicksight.types.data_label_types

        out["DataLabelTypes"] = (
            aws_sdk_quicksight.types.data_label_types.serialize_json(
                value["data_label_types"]
            )
        )
    if "position" in value:
        import aws_sdk_quicksight.types.data_label_position

        out["Position"] = aws_sdk_quicksight.types.data_label_position.serialize_json(
            value["position"]
        )
    if "label_content" in value:
        import aws_sdk_quicksight.types.data_label_content

        out["LabelContent"] = (
            aws_sdk_quicksight.types.data_label_content.serialize_json(
                value["label_content"]
            )
        )
    if "label_font_configuration" in value:
        import aws_sdk_quicksight.types.font_configuration

        out["LabelFontConfiguration"] = (
            aws_sdk_quicksight.types.font_configuration.serialize_json(
                value["label_font_configuration"]
            )
        )
    if "label_color" in value:
        out["LabelColor"] = value["label_color"]
    if "overlap" in value:
        import aws_sdk_quicksight.types.data_label_overlap

        out["Overlap"] = aws_sdk_quicksight.types.data_label_overlap.serialize_json(
            value["overlap"]
        )
    if "totals_visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["TotalsVisibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["totals_visibility"]
        )
    return out


def deserialize_json(data: dict) -> DataLabelOptions:
    out: DataLabelOptions = {}  # type: ignore[typeddict-item]
    if "Visibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "CategoryLabelVisibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["category_label_visibility"] = (
            aws_sdk_quicksight.types.visibility.deserialize_json(
                data["CategoryLabelVisibility"]
            )
        )
    if "MeasureLabelVisibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["measure_label_visibility"] = (
            aws_sdk_quicksight.types.visibility.deserialize_json(
                data["MeasureLabelVisibility"]
            )
        )
    if "DataLabelTypes" in data:
        import aws_sdk_quicksight.types.data_label_types

        out["data_label_types"] = (
            aws_sdk_quicksight.types.data_label_types.deserialize_json(
                data["DataLabelTypes"]
            )
        )
    if "Position" in data:
        import aws_sdk_quicksight.types.data_label_position

        out["position"] = aws_sdk_quicksight.types.data_label_position.deserialize_json(
            data["Position"]
        )
    if "LabelContent" in data:
        import aws_sdk_quicksight.types.data_label_content

        out["label_content"] = (
            aws_sdk_quicksight.types.data_label_content.deserialize_json(
                data["LabelContent"]
            )
        )
    if "LabelFontConfiguration" in data:
        import aws_sdk_quicksight.types.font_configuration

        out["label_font_configuration"] = (
            aws_sdk_quicksight.types.font_configuration.deserialize_json(
                data["LabelFontConfiguration"]
            )
        )
    if "LabelColor" in data:
        out["label_color"] = data["LabelColor"]
    if "Overlap" in data:
        import aws_sdk_quicksight.types.data_label_overlap

        out["overlap"] = aws_sdk_quicksight.types.data_label_overlap.deserialize_json(
            data["Overlap"]
        )
    if "TotalsVisibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["totals_visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["TotalsVisibility"]
        )
    return out
