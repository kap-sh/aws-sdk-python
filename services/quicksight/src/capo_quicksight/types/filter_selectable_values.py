"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterSelectableValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.parameter_selectable_value_list


class FilterSelectableValues(TypedDict, closed=True):
    values: NotRequired[
        "capo_quicksight.types.parameter_selectable_value_list.ParameterSelectableValueList"
    ]
    """<p>The values that are used in the <code>FilterSelectableValues</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterSelectableValues) -> dict:
    out: dict = {}
    if "values" in value:
        import capo_quicksight.types.parameter_selectable_value_list

        out["Values"] = (
            capo_quicksight.types.parameter_selectable_value_list.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterSelectableValues:
    out: FilterSelectableValues = {}  # type: ignore[typeddict-item]
    if "Values" in data:
        import capo_quicksight.types.parameter_selectable_value_list

        out["values"] = (
            capo_quicksight.types.parameter_selectable_value_list.deserialize_json(
                data["Values"]
            )
        )
    return out
