"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnTooltipItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.aggregation_function
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.string
    import capo_quicksight.types.tooltip_target
    import capo_quicksight.types.visibility


class ColumnTooltipItem(TypedDict, closed=True):
    column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The target column of the tooltip item.</p>"""
    label: NotRequired["capo_quicksight.types.string.String"]
    """<p>The label of the tooltip item.</p>"""
    visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The visibility of the tooltip item.</p>"""
    aggregation: NotRequired[
        "capo_quicksight.types.aggregation_function.AggregationFunction"
    ]
    """<p>The aggregation function of the column tooltip item.</p>"""
    tooltip_target: NotRequired["capo_quicksight.types.tooltip_target.TooltipTarget"]
    """<p>Determines the target of the column tooltip item in a combo chart visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnTooltipItem) -> dict:
    out: dict = {}
    import capo_quicksight.types.column_identifier

    out["Column"] = capo_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "label" in value:
        out["Label"] = value["label"]
    if "visibility" in value:
        import capo_quicksight.types.visibility

        out["Visibility"] = capo_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "aggregation" in value:
        import capo_quicksight.types.aggregation_function

        out["Aggregation"] = capo_quicksight.types.aggregation_function.serialize_json(
            value["aggregation"]
        )
    if "tooltip_target" in value:
        import capo_quicksight.types.tooltip_target

        out["TooltipTarget"] = capo_quicksight.types.tooltip_target.serialize_json(
            value["tooltip_target"]
        )
    return out


def deserialize_json(data: dict) -> ColumnTooltipItem:
    out: ColumnTooltipItem = {}  # type: ignore[typeddict-item]
    if "Column" in data:
        import capo_quicksight.types.column_identifier

        out["column"] = capo_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("ColumnTooltipItem.column required")
    if "Label" in data:
        out["label"] = data["Label"]
    if "Visibility" in data:
        import capo_quicksight.types.visibility

        out["visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "Aggregation" in data:
        import capo_quicksight.types.aggregation_function

        out["aggregation"] = (
            capo_quicksight.types.aggregation_function.deserialize_json(
                data["Aggregation"]
            )
        )
    if "TooltipTarget" in data:
        import capo_quicksight.types.tooltip_target

        out["tooltip_target"] = capo_quicksight.types.tooltip_target.deserialize_json(
            data["TooltipTarget"]
        )
    return out
