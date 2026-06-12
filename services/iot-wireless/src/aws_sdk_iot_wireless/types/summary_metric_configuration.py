"""Generated from Smithy shape ``com.amazonaws.iotwireless#SummaryMetricConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.summary_metric_configuration_status


class SummaryMetricConfiguration(TypedDict):
    status: NotRequired[
        "aws_sdk_iot_wireless.types.summary_metric_configuration_status.SummaryMetricConfigurationStatus"
    ]
    """<p>The status of the configuration of summary metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SummaryMetricConfiguration) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_iot_wireless.types.summary_metric_configuration_status

        out["Status"] = (
            aws_sdk_iot_wireless.types.summary_metric_configuration_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> SummaryMetricConfiguration:
    out: SummaryMetricConfiguration = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_iot_wireless.types.summary_metric_configuration_status

        out["status"] = (
            aws_sdk_iot_wireless.types.summary_metric_configuration_status.deserialize_json(
                data["Status"]
            )
        )
    return out
