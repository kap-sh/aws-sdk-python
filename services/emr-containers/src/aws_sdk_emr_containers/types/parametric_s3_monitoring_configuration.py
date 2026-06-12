"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ParametricS3MonitoringConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.uri_string


class ParametricS3MonitoringConfiguration(TypedDict):
    log_uri: NotRequired["aws_sdk_emr_containers.types.uri_string.UriString"]
    """<p>Amazon S3 destination URI for log publishing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParametricS3MonitoringConfiguration) -> dict:
    out: dict = {}
    if "log_uri" in value:
        out["logUri"] = value["log_uri"]
    return out


def deserialize_json(data: dict) -> ParametricS3MonitoringConfiguration:
    out: ParametricS3MonitoringConfiguration = {}  # type: ignore[typeddict-item]
    if "logUri" in data:
        out["log_uri"] = data["logUri"]
    return out
