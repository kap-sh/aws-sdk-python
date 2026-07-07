"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#MetricsBackupConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.region


class MetricsBackupConfiguration(TypedDict, closed=True):
    region: "aws_sdk_observabilityadmin.types.region.Region"
    """<p>Metrics specific backup destination region within the primary destination account to which metrics data should be centralized.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricsBackupConfiguration) -> dict:
    out: dict = {}
    out["Region"] = value["region"]
    return out


def deserialize_json(data: dict) -> MetricsBackupConfiguration:
    out: MetricsBackupConfiguration = {}  # type: ignore[typeddict-item]
    if "Region" in data:
        out["region"] = data["Region"]
    else:
        raise DeserializationError("MetricsBackupConfiguration.region required")
    return out
