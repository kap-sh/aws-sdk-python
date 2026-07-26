"""Generated from Smithy shape ``com.amazonaws.iotwireless#SummaryMetricConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.summary_metric_configuration_status


class SummaryMetricConfiguration(TypedDict, closed=True):
    status: NotRequired[
        "capo_iot_wireless.types.summary_metric_configuration_status.SummaryMetricConfigurationStatus"
    ]
    """<p>The status of the configuration of summary metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SummaryMetricConfiguration) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_iot_wireless.types.summary_metric_configuration_status

        out["Status"] = (
            capo_iot_wireless.types.summary_metric_configuration_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> SummaryMetricConfiguration:
    out: SummaryMetricConfiguration = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_iot_wireless.types.summary_metric_configuration_status

        out["status"] = (
            capo_iot_wireless.types.summary_metric_configuration_status.deserialize_json(
                data["Status"]
            )
        )
    return out
