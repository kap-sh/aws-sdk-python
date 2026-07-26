"""Generated from Smithy shape ``com.amazonaws.quicksight#DimensionField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.categorical_dimension_field
    import capo_quicksight.types.date_dimension_field
    import capo_quicksight.types.numerical_dimension_field


class DimensionField(TypedDict, closed=True):
    numerical_dimension_field: NotRequired[
        "capo_quicksight.types.numerical_dimension_field.NumericalDimensionField"
    ]
    """<p>The dimension type field with numerical type columns.</p>"""
    categorical_dimension_field: NotRequired[
        "capo_quicksight.types.categorical_dimension_field.CategoricalDimensionField"
    ]
    """<p>The dimension type field with categorical type columns.</p>"""
    date_dimension_field: NotRequired[
        "capo_quicksight.types.date_dimension_field.DateDimensionField"
    ]
    """<p>The dimension type field with date type columns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DimensionField) -> dict:
    out: dict = {}
    if "numerical_dimension_field" in value:
        import capo_quicksight.types.numerical_dimension_field

        out["NumericalDimensionField"] = (
            capo_quicksight.types.numerical_dimension_field.serialize_json(
                value["numerical_dimension_field"]
            )
        )
    if "categorical_dimension_field" in value:
        import capo_quicksight.types.categorical_dimension_field

        out["CategoricalDimensionField"] = (
            capo_quicksight.types.categorical_dimension_field.serialize_json(
                value["categorical_dimension_field"]
            )
        )
    if "date_dimension_field" in value:
        import capo_quicksight.types.date_dimension_field

        out["DateDimensionField"] = (
            capo_quicksight.types.date_dimension_field.serialize_json(
                value["date_dimension_field"]
            )
        )
    return out


def deserialize_json(data: dict) -> DimensionField:
    out: DimensionField = {}  # type: ignore[typeddict-item]
    if "NumericalDimensionField" in data:
        import capo_quicksight.types.numerical_dimension_field

        out["numerical_dimension_field"] = (
            capo_quicksight.types.numerical_dimension_field.deserialize_json(
                data["NumericalDimensionField"]
            )
        )
    if "CategoricalDimensionField" in data:
        import capo_quicksight.types.categorical_dimension_field

        out["categorical_dimension_field"] = (
            capo_quicksight.types.categorical_dimension_field.deserialize_json(
                data["CategoricalDimensionField"]
            )
        )
    if "DateDimensionField" in data:
        import capo_quicksight.types.date_dimension_field

        out["date_dimension_field"] = (
            capo_quicksight.types.date_dimension_field.deserialize_json(
                data["DateDimensionField"]
            )
        )
    return out
