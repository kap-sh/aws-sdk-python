"""Generated from Smithy shape ``com.amazonaws.quicksight#DatasetParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.date_time_dataset_parameter
    import capo_quicksight.types.decimal_dataset_parameter
    import capo_quicksight.types.integer_dataset_parameter
    import capo_quicksight.types.string_dataset_parameter


class DatasetParameter(TypedDict, closed=True):
    string_dataset_parameter: NotRequired[
        "capo_quicksight.types.string_dataset_parameter.StringDatasetParameter"
    ]
    """<p>A string parameter that is created in the dataset.</p>"""
    decimal_dataset_parameter: NotRequired[
        "capo_quicksight.types.decimal_dataset_parameter.DecimalDatasetParameter"
    ]
    """<p>A decimal parameter that is created in the dataset.</p>"""
    integer_dataset_parameter: NotRequired[
        "capo_quicksight.types.integer_dataset_parameter.IntegerDatasetParameter"
    ]
    """<p>An integer parameter that is created in the dataset.</p>"""
    date_time_dataset_parameter: NotRequired[
        "capo_quicksight.types.date_time_dataset_parameter.DateTimeDatasetParameter"
    ]
    """<p>A date time parameter that is created in the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetParameter) -> dict:
    out: dict = {}
    if "string_dataset_parameter" in value:
        import capo_quicksight.types.string_dataset_parameter

        out["StringDatasetParameter"] = (
            capo_quicksight.types.string_dataset_parameter.serialize_json(
                value["string_dataset_parameter"]
            )
        )
    if "decimal_dataset_parameter" in value:
        import capo_quicksight.types.decimal_dataset_parameter

        out["DecimalDatasetParameter"] = (
            capo_quicksight.types.decimal_dataset_parameter.serialize_json(
                value["decimal_dataset_parameter"]
            )
        )
    if "integer_dataset_parameter" in value:
        import capo_quicksight.types.integer_dataset_parameter

        out["IntegerDatasetParameter"] = (
            capo_quicksight.types.integer_dataset_parameter.serialize_json(
                value["integer_dataset_parameter"]
            )
        )
    if "date_time_dataset_parameter" in value:
        import capo_quicksight.types.date_time_dataset_parameter

        out["DateTimeDatasetParameter"] = (
            capo_quicksight.types.date_time_dataset_parameter.serialize_json(
                value["date_time_dataset_parameter"]
            )
        )
    return out


def deserialize_json(data: dict) -> DatasetParameter:
    out: DatasetParameter = {}  # type: ignore[typeddict-item]
    if "StringDatasetParameter" in data:
        import capo_quicksight.types.string_dataset_parameter

        out["string_dataset_parameter"] = (
            capo_quicksight.types.string_dataset_parameter.deserialize_json(
                data["StringDatasetParameter"]
            )
        )
    if "DecimalDatasetParameter" in data:
        import capo_quicksight.types.decimal_dataset_parameter

        out["decimal_dataset_parameter"] = (
            capo_quicksight.types.decimal_dataset_parameter.deserialize_json(
                data["DecimalDatasetParameter"]
            )
        )
    if "IntegerDatasetParameter" in data:
        import capo_quicksight.types.integer_dataset_parameter

        out["integer_dataset_parameter"] = (
            capo_quicksight.types.integer_dataset_parameter.deserialize_json(
                data["IntegerDatasetParameter"]
            )
        )
    if "DateTimeDatasetParameter" in data:
        import capo_quicksight.types.date_time_dataset_parameter

        out["date_time_dataset_parameter"] = (
            capo_quicksight.types.date_time_dataset_parameter.deserialize_json(
                data["DateTimeDatasetParameter"]
            )
        )
    return out
