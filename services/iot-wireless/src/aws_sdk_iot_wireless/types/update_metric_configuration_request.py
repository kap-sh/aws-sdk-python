"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdateMetricConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.summary_metric_configuration


class UpdateMetricConfigurationRequest(TypedDict, closed=True):
    summary_metric: NotRequired[
        "aws_sdk_iot_wireless.types.summary_metric_configuration.SummaryMetricConfiguration"
    ]
    """<p>The value to be used to set summary metric configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMetricConfigurationRequest) -> dict:
    out: dict = {}
    if "summary_metric" in value:
        import aws_sdk_iot_wireless.types.summary_metric_configuration

        out["SummaryMetric"] = (
            aws_sdk_iot_wireless.types.summary_metric_configuration.serialize_json(
                value["summary_metric"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateMetricConfigurationRequest:
    out: UpdateMetricConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "SummaryMetric" in data:
        import aws_sdk_iot_wireless.types.summary_metric_configuration

        out["summary_metric"] = (
            aws_sdk_iot_wireless.types.summary_metric_configuration.deserialize_json(
                data["SummaryMetric"]
            )
        )
    return out
