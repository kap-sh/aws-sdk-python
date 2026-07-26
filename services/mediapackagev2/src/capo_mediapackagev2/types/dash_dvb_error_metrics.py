"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashDvbErrorMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.dash_dvb_metrics_reporting

DashDvbErrorMetrics: TypeAlias = list[
    "capo_mediapackagev2.types.dash_dvb_metrics_reporting.DashDvbMetricsReporting"
]


# --- restJson1 ser/de ---
def serialize_json(value: DashDvbErrorMetrics) -> list:
    import capo_mediapackagev2.types.dash_dvb_metrics_reporting

    out: list = []
    for item in value:
        out.append(
            capo_mediapackagev2.types.dash_dvb_metrics_reporting.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DashDvbErrorMetrics:
    import capo_mediapackagev2.types.dash_dvb_metrics_reporting

    out: DashDvbErrorMetrics = []
    for item in data:
        out.append(
            capo_mediapackagev2.types.dash_dvb_metrics_reporting.deserialize_json(item)
        )
    return out
