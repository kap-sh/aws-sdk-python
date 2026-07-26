"""Generated from Smithy shape ``com.amazonaws.quicksight#DecimalDatasetParameterDefaultValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.decimal_dataset_parameter_value_list


class DecimalDatasetParameterDefaultValues(TypedDict, closed=True):
    static_values: NotRequired[
        "capo_quicksight.types.decimal_dataset_parameter_value_list.DecimalDatasetParameterValueList"
    ]
    """<p>A list of static default values for a given decimal parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DecimalDatasetParameterDefaultValues) -> dict:
    out: dict = {}
    if "static_values" in value:
        import capo_quicksight.types.decimal_dataset_parameter_value_list

        out["StaticValues"] = (
            capo_quicksight.types.decimal_dataset_parameter_value_list.serialize_json(
                value["static_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> DecimalDatasetParameterDefaultValues:
    out: DecimalDatasetParameterDefaultValues = {}  # type: ignore[typeddict-item]
    if "StaticValues" in data:
        import capo_quicksight.types.decimal_dataset_parameter_value_list

        out["static_values"] = (
            capo_quicksight.types.decimal_dataset_parameter_value_list.deserialize_json(
                data["StaticValues"]
            )
        )
    return out
