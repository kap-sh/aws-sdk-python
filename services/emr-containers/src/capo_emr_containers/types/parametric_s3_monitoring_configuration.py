"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ParametricS3MonitoringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.uri_string


class ParametricS3MonitoringConfiguration(TypedDict, closed=True):
    log_uri: NotRequired["capo_emr_containers.types.uri_string.UriString"]
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
