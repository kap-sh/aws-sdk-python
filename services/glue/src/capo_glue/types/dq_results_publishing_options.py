"""Generated from Smithy shape ``com.amazonaws.glue#DQResultsPublishingOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.boxed_boolean
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.generic_limited_string


class DQResultsPublishingOptions(TypedDict, closed=True):
    evaluation_context: NotRequired[
        "capo_glue.types.generic_limited_string.GenericLimitedString"
    ]
    """<p>The context of the evaluation.</p>"""
    results_s3_prefix: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The Amazon S3 prefix prepended to the results.</p>"""
    cloud_watch_metrics_enabled: NotRequired[
        "capo_glue.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Enable metrics for your data quality results.</p>"""
    results_publishing_enabled: NotRequired[
        "capo_glue.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Enable publishing for your data quality results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DQResultsPublishingOptions) -> dict:
    out: dict = {}
    if "evaluation_context" in value:
        out["EvaluationContext"] = value["evaluation_context"]
    if "results_s3_prefix" in value:
        out["ResultsS3Prefix"] = value["results_s3_prefix"]
    if "cloud_watch_metrics_enabled" in value:
        out["CloudWatchMetricsEnabled"] = value["cloud_watch_metrics_enabled"]
    if "results_publishing_enabled" in value:
        out["ResultsPublishingEnabled"] = value["results_publishing_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DQResultsPublishingOptions:
    out: DQResultsPublishingOptions = {}  # type: ignore[typeddict-item]
    if "EvaluationContext" in data:
        out["evaluation_context"] = data["EvaluationContext"]
    if "ResultsS3Prefix" in data:
        out["results_s3_prefix"] = data["ResultsS3Prefix"]
    if "CloudWatchMetricsEnabled" in data:
        out["cloud_watch_metrics_enabled"] = data["CloudWatchMetricsEnabled"]
    if "ResultsPublishingEnabled" in data:
        out["results_publishing_enabled"] = data["ResultsPublishingEnabled"]
    return out
