"""Generated from Smithy shape ``com.amazonaws.quicksight#ParameterSelectableValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.parameter_selectable_value_list


class ParameterSelectableValues(TypedDict, closed=True):
    values: NotRequired[
        "capo_quicksight.types.parameter_selectable_value_list.ParameterSelectableValueList"
    ]
    """<p>The values that are used in <code>ParameterSelectableValues</code>.</p>"""
    link_to_data_set_column: NotRequired[
        "capo_quicksight.types.column_identifier.ColumnIdentifier"
    ]
    """<p>The column identifier that fetches values from the data set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParameterSelectableValues) -> dict:
    out: dict = {}
    if "values" in value:
        import capo_quicksight.types.parameter_selectable_value_list

        out["Values"] = (
            capo_quicksight.types.parameter_selectable_value_list.serialize_json(
                value["values"]
            )
        )
    if "link_to_data_set_column" in value:
        import capo_quicksight.types.column_identifier

        out["LinkToDataSetColumn"] = (
            capo_quicksight.types.column_identifier.serialize_json(
                value["link_to_data_set_column"]
            )
        )
    return out


def deserialize_json(data: dict) -> ParameterSelectableValues:
    out: ParameterSelectableValues = {}  # type: ignore[typeddict-item]
    if "Values" in data:
        import capo_quicksight.types.parameter_selectable_value_list

        out["values"] = (
            capo_quicksight.types.parameter_selectable_value_list.deserialize_json(
                data["Values"]
            )
        )
    if "LinkToDataSetColumn" in data:
        import capo_quicksight.types.column_identifier

        out["link_to_data_set_column"] = (
            capo_quicksight.types.column_identifier.deserialize_json(
                data["LinkToDataSetColumn"]
            )
        )
    return out
