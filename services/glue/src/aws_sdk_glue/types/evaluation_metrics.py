"""Generated from Smithy shape ``com.amazonaws.glue#EvaluationMetrics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.find_matches_metrics
    import aws_sdk_glue.types.transform_type


class EvaluationMetrics(TypedDict):
    transform_type: "aws_sdk_glue.types.transform_type.TransformType"
    """<p>The type of machine learning transform.</p>"""
    find_matches_metrics: NotRequired[
        "aws_sdk_glue.types.find_matches_metrics.FindMatchesMetrics"
    ]
    """<p>The evaluation metrics for the find matches algorithm.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluationMetrics) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.transform_type

    out["TransformType"] = aws_sdk_glue.types.transform_type.serialize_aws_json_1_1(
        value["transform_type"]
    )
    if "find_matches_metrics" in value:
        import aws_sdk_glue.types.find_matches_metrics

        out["FindMatchesMetrics"] = (
            aws_sdk_glue.types.find_matches_metrics.serialize_aws_json_1_1(
                value["find_matches_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluationMetrics:
    out: EvaluationMetrics = {}  # type: ignore[typeddict-item]
    if "TransformType" in data:
        import aws_sdk_glue.types.transform_type

        out["transform_type"] = (
            aws_sdk_glue.types.transform_type.deserialize_aws_json_1_1(
                data["TransformType"]
            )
        )
    else:
        raise DeserializationError("EvaluationMetrics.transform_type required")
    if "FindMatchesMetrics" in data:
        import aws_sdk_glue.types.find_matches_metrics

        out["find_matches_metrics"] = (
            aws_sdk_glue.types.find_matches_metrics.deserialize_aws_json_1_1(
                data["FindMatchesMetrics"]
            )
        )
    return out
