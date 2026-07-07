"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#MetricSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.metric_provider_arn
    import aws_sdk_compute_optimizer.types.metric_source_provider


class MetricSource(TypedDict, closed=True):
    provider: NotRequired[
        "aws_sdk_compute_optimizer.types.metric_source_provider.MetricSourceProvider"
    ]
    """<p> The name of the metric source provider. </p>"""
    provider_arn: NotRequired[
        "aws_sdk_compute_optimizer.types.metric_provider_arn.MetricProviderArn"
    ]
    """<p> The ARN of the metric source provider. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricSource) -> dict:
    out: dict = {}
    if "provider" in value:
        import aws_sdk_compute_optimizer.types.metric_source_provider

        out["provider"] = (
            aws_sdk_compute_optimizer.types.metric_source_provider.serialize_aws_json_1_0(
                value["provider"]
            )
        )
    if "provider_arn" in value:
        out["providerArn"] = value["provider_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MetricSource:
    out: MetricSource = {}  # type: ignore[typeddict-item]
    if "provider" in data:
        import aws_sdk_compute_optimizer.types.metric_source_provider

        out["provider"] = (
            aws_sdk_compute_optimizer.types.metric_source_provider.deserialize_aws_json_1_0(
                data["provider"]
            )
        )
    if "providerArn" in data:
        out["provider_arn"] = data["providerArn"]
    return out
