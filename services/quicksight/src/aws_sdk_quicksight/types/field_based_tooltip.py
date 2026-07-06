"""Generated from Smithy shape ``com.amazonaws.quicksight#FieldBasedTooltip``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.tooltip_item_list
    import aws_sdk_quicksight.types.tooltip_title_type
    import aws_sdk_quicksight.types.visibility


class FieldBasedTooltip(TypedDict, closed=True):
    aggregation_visibility: NotRequired[
        "aws_sdk_quicksight.types.visibility.Visibility"
    ]
    """<p>The visibility of <code>Show aggregations</code>.</p>"""
    tooltip_title_type: NotRequired[
        "aws_sdk_quicksight.types.tooltip_title_type.TooltipTitleType"
    ]
    """<p>The type for the >tooltip title. Choose one of the following options:</p> <ul> <li> <p> <code>NONE</code>: Doesn't use the primary value as the title.</p> </li> <li> <p> <code>PRIMARY_VALUE</code>: Uses primary value as the title.</p> </li> </ul>"""
    tooltip_fields: NotRequired[
        "aws_sdk_quicksight.types.tooltip_item_list.TooltipItemList"
    ]
    """<p>The fields configuration in the tooltip.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldBasedTooltip) -> dict:
    out: dict = {}
    if "aggregation_visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["AggregationVisibility"] = (
            aws_sdk_quicksight.types.visibility.serialize_json(
                value["aggregation_visibility"]
            )
        )
    if "tooltip_title_type" in value:
        import aws_sdk_quicksight.types.tooltip_title_type

        out["TooltipTitleType"] = (
            aws_sdk_quicksight.types.tooltip_title_type.serialize_json(
                value["tooltip_title_type"]
            )
        )
    if "tooltip_fields" in value:
        import aws_sdk_quicksight.types.tooltip_item_list

        out["TooltipFields"] = (
            aws_sdk_quicksight.types.tooltip_item_list.serialize_json(
                value["tooltip_fields"]
            )
        )
    return out


def deserialize_json(data: dict) -> FieldBasedTooltip:
    out: FieldBasedTooltip = {}  # type: ignore[typeddict-item]
    if "AggregationVisibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["aggregation_visibility"] = (
            aws_sdk_quicksight.types.visibility.deserialize_json(
                data["AggregationVisibility"]
            )
        )
    if "TooltipTitleType" in data:
        import aws_sdk_quicksight.types.tooltip_title_type

        out["tooltip_title_type"] = (
            aws_sdk_quicksight.types.tooltip_title_type.deserialize_json(
                data["TooltipTitleType"]
            )
        )
    if "TooltipFields" in data:
        import aws_sdk_quicksight.types.tooltip_item_list

        out["tooltip_fields"] = (
            aws_sdk_quicksight.types.tooltip_item_list.deserialize_json(
                data["TooltipFields"]
            )
        )
    return out
