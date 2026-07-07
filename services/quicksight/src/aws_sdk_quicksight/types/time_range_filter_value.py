"""Generated from Smithy shape ``com.amazonaws.quicksight#TimeRangeFilterValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.parameter_name
    import aws_sdk_quicksight.types.rolling_date_configuration
    import aws_sdk_quicksight.types.timestamp


class TimeRangeFilterValue(TypedDict, closed=True):
    static_value: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The static input value.</p>"""
    rolling_date: NotRequired[
        "aws_sdk_quicksight.types.rolling_date_configuration.RollingDateConfiguration"
    ]
    """<p>The rolling date input value.</p>"""
    parameter: NotRequired["aws_sdk_quicksight.types.parameter_name.ParameterName"]
    """<p>The parameter type input value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeRangeFilterValue) -> dict:
    out: dict = {}
    if "static_value" in value:
        import aws_sdk_quicksight.types.timestamp

        out["StaticValue"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["static_value"]
        )
    if "rolling_date" in value:
        import aws_sdk_quicksight.types.rolling_date_configuration

        out["RollingDate"] = (
            aws_sdk_quicksight.types.rolling_date_configuration.serialize_json(
                value["rolling_date"]
            )
        )
    if "parameter" in value:
        out["Parameter"] = value["parameter"]
    return out


def deserialize_json(data: dict) -> TimeRangeFilterValue:
    out: TimeRangeFilterValue = {}  # type: ignore[typeddict-item]
    if "StaticValue" in data:
        import aws_sdk_quicksight.types.timestamp

        out["static_value"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["StaticValue"]
        )
    if "RollingDate" in data:
        import aws_sdk_quicksight.types.rolling_date_configuration

        out["rolling_date"] = (
            aws_sdk_quicksight.types.rolling_date_configuration.deserialize_json(
                data["RollingDate"]
            )
        )
    if "Parameter" in data:
        out["parameter"] = data["Parameter"]
    return out
