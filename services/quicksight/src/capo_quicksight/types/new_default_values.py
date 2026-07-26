"""Generated from Smithy shape ``com.amazonaws.quicksight#NewDefaultValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.date_time_dataset_parameter_value_list
    import capo_quicksight.types.decimal_dataset_parameter_value_list
    import capo_quicksight.types.integer_dataset_parameter_value_list
    import capo_quicksight.types.string_dataset_parameter_value_list


class NewDefaultValues(TypedDict, closed=True):
    string_static_values: NotRequired[
        "capo_quicksight.types.string_dataset_parameter_value_list.StringDatasetParameterValueList"
    ]
    """<p>A list of static default values for a given string parameter.</p>"""
    decimal_static_values: NotRequired[
        "capo_quicksight.types.decimal_dataset_parameter_value_list.DecimalDatasetParameterValueList"
    ]
    """<p>A list of static default values for a given decimal parameter.</p>"""
    date_time_static_values: NotRequired[
        "capo_quicksight.types.date_time_dataset_parameter_value_list.DateTimeDatasetParameterValueList"
    ]
    """<p>A list of static default values for a given date time parameter.</p>"""
    integer_static_values: NotRequired[
        "capo_quicksight.types.integer_dataset_parameter_value_list.IntegerDatasetParameterValueList"
    ]
    """<p>A list of static default values for a given integer parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NewDefaultValues) -> dict:
    out: dict = {}
    if "string_static_values" in value:
        import capo_quicksight.types.string_dataset_parameter_value_list

        out["StringStaticValues"] = (
            capo_quicksight.types.string_dataset_parameter_value_list.serialize_json(
                value["string_static_values"]
            )
        )
    if "decimal_static_values" in value:
        import capo_quicksight.types.decimal_dataset_parameter_value_list

        out["DecimalStaticValues"] = (
            capo_quicksight.types.decimal_dataset_parameter_value_list.serialize_json(
                value["decimal_static_values"]
            )
        )
    if "date_time_static_values" in value:
        import capo_quicksight.types.date_time_dataset_parameter_value_list

        out["DateTimeStaticValues"] = (
            capo_quicksight.types.date_time_dataset_parameter_value_list.serialize_json(
                value["date_time_static_values"]
            )
        )
    if "integer_static_values" in value:
        import capo_quicksight.types.integer_dataset_parameter_value_list

        out["IntegerStaticValues"] = (
            capo_quicksight.types.integer_dataset_parameter_value_list.serialize_json(
                value["integer_static_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> NewDefaultValues:
    out: NewDefaultValues = {}  # type: ignore[typeddict-item]
    if "StringStaticValues" in data:
        import capo_quicksight.types.string_dataset_parameter_value_list

        out["string_static_values"] = (
            capo_quicksight.types.string_dataset_parameter_value_list.deserialize_json(
                data["StringStaticValues"]
            )
        )
    if "DecimalStaticValues" in data:
        import capo_quicksight.types.decimal_dataset_parameter_value_list

        out["decimal_static_values"] = (
            capo_quicksight.types.decimal_dataset_parameter_value_list.deserialize_json(
                data["DecimalStaticValues"]
            )
        )
    if "DateTimeStaticValues" in data:
        import capo_quicksight.types.date_time_dataset_parameter_value_list

        out["date_time_static_values"] = (
            capo_quicksight.types.date_time_dataset_parameter_value_list.deserialize_json(
                data["DateTimeStaticValues"]
            )
        )
    if "IntegerStaticValues" in data:
        import capo_quicksight.types.integer_dataset_parameter_value_list

        out["integer_static_values"] = (
            capo_quicksight.types.integer_dataset_parameter_value_list.deserialize_json(
                data["IntegerStaticValues"]
            )
        )
    return out
