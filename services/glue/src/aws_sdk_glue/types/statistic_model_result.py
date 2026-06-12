"""Generated from Smithy shape ``com.amazonaws.glue#StatisticModelResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.inclusion_annotation_value
    import aws_sdk_glue.types.nullable_double
    import aws_sdk_glue.types.timestamp


class StatisticModelResult(TypedDict):
    lower_bound: NotRequired["aws_sdk_glue.types.nullable_double.NullableDouble"]
    """<p>The lower bound.</p>"""
    upper_bound: NotRequired["aws_sdk_glue.types.nullable_double.NullableDouble"]
    """<p>The upper bound.</p>"""
    predicted_value: NotRequired["aws_sdk_glue.types.nullable_double.NullableDouble"]
    """<p>The predicted value.</p>"""
    actual_value: NotRequired["aws_sdk_glue.types.nullable_double.NullableDouble"]
    """<p>The actual value.</p>"""
    date: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The date.</p>"""
    inclusion_annotation: NotRequired[
        "aws_sdk_glue.types.inclusion_annotation_value.InclusionAnnotationValue"
    ]
    """<p>The inclusion annotation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatisticModelResult) -> dict:
    out: dict = {}
    if "lower_bound" in value:
        out["LowerBound"] = value["lower_bound"]
    if "upper_bound" in value:
        out["UpperBound"] = value["upper_bound"]
    if "predicted_value" in value:
        out["PredictedValue"] = value["predicted_value"]
    if "actual_value" in value:
        out["ActualValue"] = value["actual_value"]
    if "date" in value:
        import aws_sdk_glue.types.timestamp

        out["Date"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(value["date"])
    if "inclusion_annotation" in value:
        import aws_sdk_glue.types.inclusion_annotation_value

        out["InclusionAnnotation"] = (
            aws_sdk_glue.types.inclusion_annotation_value.serialize_aws_json_1_1(
                value["inclusion_annotation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StatisticModelResult:
    out: StatisticModelResult = {}  # type: ignore[typeddict-item]
    if "LowerBound" in data:
        out["lower_bound"] = data["LowerBound"]
    if "UpperBound" in data:
        out["upper_bound"] = data["UpperBound"]
    if "PredictedValue" in data:
        out["predicted_value"] = data["PredictedValue"]
    if "ActualValue" in data:
        out["actual_value"] = data["ActualValue"]
    if "Date" in data:
        import aws_sdk_glue.types.timestamp

        out["date"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["Date"]
        )
    if "InclusionAnnotation" in data:
        import aws_sdk_glue.types.inclusion_annotation_value

        out["inclusion_annotation"] = (
            aws_sdk_glue.types.inclusion_annotation_value.deserialize_aws_json_1_1(
                data["InclusionAnnotation"]
            )
        )
    return out
