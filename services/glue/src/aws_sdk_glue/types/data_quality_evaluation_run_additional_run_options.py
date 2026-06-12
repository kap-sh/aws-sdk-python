"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityEvaluationRunAdditionalRunOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.dq_composite_rule_evaluation_method
    import aws_sdk_glue.types.generic_string
    import aws_sdk_glue.types.nullable_boolean
    import aws_sdk_glue.types.uri_string


class DataQualityEvaluationRunAdditionalRunOptions(TypedDict):
    cloud_watch_metrics_enabled: NotRequired[
        "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Whether or not to enable CloudWatch metrics.</p>"""
    results_s3_prefix: NotRequired["aws_sdk_glue.types.uri_string.UriString"]
    """<p>Prefix for Amazon S3 to store results.</p>"""
    composite_rule_evaluation_method: NotRequired[
        "aws_sdk_glue.types.dq_composite_rule_evaluation_method.DQCompositeRuleEvaluationMethod"
    ]
    """<p>Set the evaluation method for composite rules in the ruleset to ROW/COLUMN</p>"""
    custom_log_group_prefix: NotRequired[
        "aws_sdk_glue.types.generic_string.GenericString"
    ]
    """<p>A custom prefix for the CloudWatch log group names. When specified, evaluation run logs are written to <code><CustomLogGroupPrefix>/error</code> and <code><CustomLogGroupPrefix>/output</code> instead of the default <code>/aws-glue/data-quality/error</code> and <code>/aws-glue/data-quality/output</code> log groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityEvaluationRunAdditionalRunOptions) -> dict:
    out: dict = {}
    if "cloud_watch_metrics_enabled" in value:
        out["CloudWatchMetricsEnabled"] = value["cloud_watch_metrics_enabled"]
    if "results_s3_prefix" in value:
        out["ResultsS3Prefix"] = value["results_s3_prefix"]
    if "composite_rule_evaluation_method" in value:
        import aws_sdk_glue.types.dq_composite_rule_evaluation_method

        out["CompositeRuleEvaluationMethod"] = (
            aws_sdk_glue.types.dq_composite_rule_evaluation_method.serialize_aws_json_1_1(
                value["composite_rule_evaluation_method"]
            )
        )
    if "custom_log_group_prefix" in value:
        out["CustomLogGroupPrefix"] = value["custom_log_group_prefix"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DataQualityEvaluationRunAdditionalRunOptions:
    out: DataQualityEvaluationRunAdditionalRunOptions = {}  # type: ignore[typeddict-item]
    if "CloudWatchMetricsEnabled" in data:
        out["cloud_watch_metrics_enabled"] = data["CloudWatchMetricsEnabled"]
    if "ResultsS3Prefix" in data:
        out["results_s3_prefix"] = data["ResultsS3Prefix"]
    if "CompositeRuleEvaluationMethod" in data:
        import aws_sdk_glue.types.dq_composite_rule_evaluation_method

        out["composite_rule_evaluation_method"] = (
            aws_sdk_glue.types.dq_composite_rule_evaluation_method.deserialize_aws_json_1_1(
                data["CompositeRuleEvaluationMethod"]
            )
        )
    if "CustomLogGroupPrefix" in data:
        out["custom_log_group_prefix"] = data["CustomLogGroupPrefix"]
    return out
