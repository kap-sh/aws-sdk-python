"""Generated from Smithy shape ``com.amazonaws.quicksight#ComparativeOrder``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_ordering_type
    import aws_sdk_quicksight.types.string_list
    import aws_sdk_quicksight.types.undefined_specified_value_type


class ComparativeOrder(TypedDict):
    use_ordering: NotRequired[
        "aws_sdk_quicksight.types.column_ordering_type.ColumnOrderingType"
    ]
    """<p>The ordering type for a column. Valid values for this structure are <code>GREATER_IS_BETTER</code>, <code>LESSER_IS_BETTER</code> and <code>SPECIFIED</code>.</p>"""
    specifed_order: NotRequired["aws_sdk_quicksight.types.string_list.StringList"]
    """<p>The list of columns to be used in the ordering.</p>"""
    treat_undefined_specified_values: NotRequired[
        "aws_sdk_quicksight.types.undefined_specified_value_type.UndefinedSpecifiedValueType"
    ]
    """<p>The treat of undefined specified values. Valid values for this structure are <code>LEAST</code> and <code>MOST</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComparativeOrder) -> dict:
    out: dict = {}
    if "use_ordering" in value:
        import aws_sdk_quicksight.types.column_ordering_type

        out["UseOrdering"] = (
            aws_sdk_quicksight.types.column_ordering_type.serialize_json(
                value["use_ordering"]
            )
        )
    if "specifed_order" in value:
        import aws_sdk_quicksight.types.string_list

        out["SpecifedOrder"] = aws_sdk_quicksight.types.string_list.serialize_json(
            value["specifed_order"]
        )
    if "treat_undefined_specified_values" in value:
        import aws_sdk_quicksight.types.undefined_specified_value_type

        out["TreatUndefinedSpecifiedValues"] = (
            aws_sdk_quicksight.types.undefined_specified_value_type.serialize_json(
                value["treat_undefined_specified_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComparativeOrder:
    out: ComparativeOrder = {}  # type: ignore[typeddict-item]
    if "UseOrdering" in data:
        import aws_sdk_quicksight.types.column_ordering_type

        out["use_ordering"] = (
            aws_sdk_quicksight.types.column_ordering_type.deserialize_json(
                data["UseOrdering"]
            )
        )
    if "SpecifedOrder" in data:
        import aws_sdk_quicksight.types.string_list

        out["specifed_order"] = aws_sdk_quicksight.types.string_list.deserialize_json(
            data["SpecifedOrder"]
        )
    if "TreatUndefinedSpecifiedValues" in data:
        import aws_sdk_quicksight.types.undefined_specified_value_type

        out["treat_undefined_specified_values"] = (
            aws_sdk_quicksight.types.undefined_specified_value_type.deserialize_json(
                data["TreatUndefinedSpecifiedValues"]
            )
        )
    return out
