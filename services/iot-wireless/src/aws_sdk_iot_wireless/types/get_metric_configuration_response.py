"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetMetricConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.summary_metric_configuration


class GetMetricConfigurationResponse(TypedDict):
    summary_metric: NotRequired[
        "aws_sdk_iot_wireless.types.summary_metric_configuration.SummaryMetricConfiguration"
    ]
    """<p>The configuration status of the AWS account for summary metric aggregation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMetricConfigurationResponse) -> dict:
    out: dict = {}
    if "summary_metric" in value:
        import aws_sdk_iot_wireless.types.summary_metric_configuration

        out["SummaryMetric"] = (
            aws_sdk_iot_wireless.types.summary_metric_configuration.serialize_json(
                value["summary_metric"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMetricConfigurationResponse:
    out: GetMetricConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "SummaryMetric" in data:
        import aws_sdk_iot_wireless.types.summary_metric_configuration

        out["summary_metric"] = (
            aws_sdk_iot_wireless.types.summary_metric_configuration.deserialize_json(
                data["SummaryMetric"]
            )
        )
    return out
