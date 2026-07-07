"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnTooltipItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aggregation_function
    import aws_sdk_quicksight.types.column_identifier
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.tooltip_target
    import aws_sdk_quicksight.types.visibility


class ColumnTooltipItem(TypedDict, closed=True):
    column: "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The target column of the tooltip item.</p>"""
    label: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The label of the tooltip item.</p>"""
    visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>The visibility of the tooltip item.</p>"""
    aggregation: NotRequired[
        "aws_sdk_quicksight.types.aggregation_function.AggregationFunction"
    ]
    """<p>The aggregation function of the column tooltip item.</p>"""
    tooltip_target: NotRequired["aws_sdk_quicksight.types.tooltip_target.TooltipTarget"]
    """<p>Determines the target of the column tooltip item in a combo chart visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnTooltipItem) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.column_identifier

    out["Column"] = aws_sdk_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "label" in value:
        out["Label"] = value["label"]
    if "visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["Visibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "aggregation" in value:
        import aws_sdk_quicksight.types.aggregation_function

        out["Aggregation"] = (
            aws_sdk_quicksight.types.aggregation_function.serialize_json(
                value["aggregation"]
            )
        )
    if "tooltip_target" in value:
        import aws_sdk_quicksight.types.tooltip_target

        out["TooltipTarget"] = aws_sdk_quicksight.types.tooltip_target.serialize_json(
            value["tooltip_target"]
        )
    return out


def deserialize_json(data: dict) -> ColumnTooltipItem:
    out: ColumnTooltipItem = {}  # type: ignore[typeddict-item]
    if "Column" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["column"] = aws_sdk_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("ColumnTooltipItem.column required")
    if "Label" in data:
        out["label"] = data["Label"]
    if "Visibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "Aggregation" in data:
        import aws_sdk_quicksight.types.aggregation_function

        out["aggregation"] = (
            aws_sdk_quicksight.types.aggregation_function.deserialize_json(
                data["Aggregation"]
            )
        )
    if "TooltipTarget" in data:
        import aws_sdk_quicksight.types.tooltip_target

        out["tooltip_target"] = (
            aws_sdk_quicksight.types.tooltip_target.deserialize_json(
                data["TooltipTarget"]
            )
        )
    return out
