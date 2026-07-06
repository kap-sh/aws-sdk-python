"""Generated from Smithy shape ``com.amazonaws.quicksight#NumericRangeFilterValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.double
    import aws_sdk_quicksight.types.parameter_name


class NumericRangeFilterValue(TypedDict, closed=True):
    static_value: NotRequired["aws_sdk_quicksight.types.double.Double"]
    """<p>The static value of the numeric range filter.</p>"""
    parameter: NotRequired["aws_sdk_quicksight.types.parameter_name.ParameterName"]
    """<p>The parameter that is used in the numeric range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumericRangeFilterValue) -> dict:
    out: dict = {}
    if "static_value" in value:
        out["StaticValue"] = value["static_value"]
    if "parameter" in value:
        out["Parameter"] = value["parameter"]
    return out


def deserialize_json(data: dict) -> NumericRangeFilterValue:
    out: NumericRangeFilterValue = {}  # type: ignore[typeddict-item]
    if "StaticValue" in data:
        out["static_value"] = data["StaticValue"]
    if "Parameter" in data:
        out["parameter"] = data["Parameter"]
    return out
