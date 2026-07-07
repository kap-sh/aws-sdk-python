"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityMetricValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.nullable_double


class DataQualityMetricValues(TypedDict, closed=True):
    actual_value: NotRequired["aws_sdk_glue.types.nullable_double.NullableDouble"]
    """<p>The actual value of the data quality metric.</p>"""
    expected_value: NotRequired["aws_sdk_glue.types.nullable_double.NullableDouble"]
    """<p>The expected value of the data quality metric according to the analysis of historical data.</p>"""
    lower_limit: NotRequired["aws_sdk_glue.types.nullable_double.NullableDouble"]
    """<p>The lower limit of the data quality metric value according to the analysis of historical data.</p>"""
    upper_limit: NotRequired["aws_sdk_glue.types.nullable_double.NullableDouble"]
    """<p>The upper limit of the data quality metric value according to the analysis of historical data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityMetricValues) -> dict:
    out: dict = {}
    if "actual_value" in value:
        out["ActualValue"] = value["actual_value"]
    if "expected_value" in value:
        out["ExpectedValue"] = value["expected_value"]
    if "lower_limit" in value:
        out["LowerLimit"] = value["lower_limit"]
    if "upper_limit" in value:
        out["UpperLimit"] = value["upper_limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityMetricValues:
    out: DataQualityMetricValues = {}  # type: ignore[typeddict-item]
    if "ActualValue" in data:
        out["actual_value"] = data["ActualValue"]
    if "ExpectedValue" in data:
        out["expected_value"] = data["ExpectedValue"]
    if "LowerLimit" in data:
        out["lower_limit"] = data["LowerLimit"]
    if "UpperLimit" in data:
        out["upper_limit"] = data["UpperLimit"]
    return out
