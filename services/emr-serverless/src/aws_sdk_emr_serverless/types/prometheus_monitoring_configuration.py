"""Generated from Smithy shape ``com.amazonaws.emrserverless#PrometheusMonitoringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.prometheus_url_string


class PrometheusMonitoringConfiguration(TypedDict, closed=True):
    remote_write_url: NotRequired[
        "aws_sdk_emr_serverless.types.prometheus_url_string.PrometheusUrlString"
    ]
    """<p>The remote write URL in the Amazon Managed Service for Prometheus workspace to send metrics to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrometheusMonitoringConfiguration) -> dict:
    out: dict = {}
    if "remote_write_url" in value:
        out["remoteWriteUrl"] = value["remote_write_url"]
    return out


def deserialize_json(data: dict) -> PrometheusMonitoringConfiguration:
    out: PrometheusMonitoringConfiguration = {}  # type: ignore[typeddict-item]
    if "remoteWriteUrl" in data:
        out["remote_write_url"] = data["remoteWriteUrl"]
    return out
