"""Generated from Smithy shape ``com.amazonaws.personalize#UpdateMetricAttributionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.metric_attributes
    import aws_sdk_personalize.types.metric_attributes_names_list
    import aws_sdk_personalize.types.metric_attribution_output


class UpdateMetricAttributionRequest(TypedDict, closed=True):
    add_metrics: NotRequired[
        "aws_sdk_personalize.types.metric_attributes.MetricAttributes"
    ]
    """<p>Add new metric attributes to the metric attribution.</p>"""
    remove_metrics: NotRequired[
        "aws_sdk_personalize.types.metric_attributes_names_list.MetricAttributesNamesList"
    ]
    """<p>Remove metric attributes from the metric attribution.</p>"""
    metrics_output_config: NotRequired[
        "aws_sdk_personalize.types.metric_attribution_output.MetricAttributionOutput"
    ]
    """<p>An output config for the metric attribution.</p>"""
    metric_attribution_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the metric attribution to update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMetricAttributionRequest) -> dict:
    out: dict = {}
    if "add_metrics" in value:
        import aws_sdk_personalize.types.metric_attributes

        out["addMetrics"] = (
            aws_sdk_personalize.types.metric_attributes.serialize_aws_json_1_1(
                value["add_metrics"]
            )
        )
    if "remove_metrics" in value:
        import aws_sdk_personalize.types.metric_attributes_names_list

        out["removeMetrics"] = (
            aws_sdk_personalize.types.metric_attributes_names_list.serialize_aws_json_1_1(
                value["remove_metrics"]
            )
        )
    if "metrics_output_config" in value:
        import aws_sdk_personalize.types.metric_attribution_output

        out["metricsOutputConfig"] = (
            aws_sdk_personalize.types.metric_attribution_output.serialize_aws_json_1_1(
                value["metrics_output_config"]
            )
        )
    if "metric_attribution_arn" in value:
        out["metricAttributionArn"] = value["metric_attribution_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMetricAttributionRequest:
    out: UpdateMetricAttributionRequest = {}  # type: ignore[typeddict-item]
    if "addMetrics" in data:
        import aws_sdk_personalize.types.metric_attributes

        out["add_metrics"] = (
            aws_sdk_personalize.types.metric_attributes.deserialize_aws_json_1_1(
                data["addMetrics"]
            )
        )
    if "removeMetrics" in data:
        import aws_sdk_personalize.types.metric_attributes_names_list

        out["remove_metrics"] = (
            aws_sdk_personalize.types.metric_attributes_names_list.deserialize_aws_json_1_1(
                data["removeMetrics"]
            )
        )
    if "metricsOutputConfig" in data:
        import aws_sdk_personalize.types.metric_attribution_output

        out["metrics_output_config"] = (
            aws_sdk_personalize.types.metric_attribution_output.deserialize_aws_json_1_1(
                data["metricsOutputConfig"]
            )
        )
    if "metricAttributionArn" in data:
        out["metric_attribution_arn"] = data["metricAttributionArn"]
    return out
