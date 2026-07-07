"""Generated from Smithy shape ``com.amazonaws.forecast#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn
    import aws_sdk_forecast.types.filter_condition_string
    import aws_sdk_forecast.types.string


class Filter(TypedDict, closed=True):
    key: "aws_sdk_forecast.types.string.String"
    """<p>The name of the parameter to filter on.</p>"""
    value: "aws_sdk_forecast.types.arn.Arn"
    """<p>The value to match.</p>"""
    condition: "aws_sdk_forecast.types.filter_condition_string.FilterConditionString"
    """<p>The condition to apply. To include the objects that match the statement, specify <code>IS</code>. To exclude matching objects, specify <code>IS_NOT</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filter) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    import aws_sdk_forecast.types.filter_condition_string

    out["Condition"] = (
        aws_sdk_forecast.types.filter_condition_string.serialize_aws_json_1_1(
            value["condition"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("Filter.key required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("Filter.value required")
    if "Condition" in data:
        import aws_sdk_forecast.types.filter_condition_string

        out["condition"] = (
            aws_sdk_forecast.types.filter_condition_string.deserialize_aws_json_1_1(
                data["Condition"]
            )
        )
    else:
        raise DeserializationError("Filter.condition required")
    return out
