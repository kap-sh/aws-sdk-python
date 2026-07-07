"""Generated from Smithy shape ``com.amazonaws.emrcontainers#S3MonitoringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_emr_containers.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.uri_string


class S3MonitoringConfiguration(TypedDict, closed=True):
    log_uri: "aws_sdk_emr_containers.types.uri_string.UriString"
    """<p>Amazon S3 destination URI for log publishing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3MonitoringConfiguration) -> dict:
    out: dict = {}
    out["logUri"] = value["log_uri"]
    return out


def deserialize_json(data: dict) -> S3MonitoringConfiguration:
    out: S3MonitoringConfiguration = {}  # type: ignore[typeddict-item]
    if "logUri" in data:
        out["log_uri"] = data["logUri"]
    else:
        raise DeserializationError("S3MonitoringConfiguration.log_uri required")
    return out
