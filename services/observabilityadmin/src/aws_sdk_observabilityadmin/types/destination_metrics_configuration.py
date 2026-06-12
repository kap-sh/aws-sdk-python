"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#DestinationMetricsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.metrics_backup_configuration


class DestinationMetricsConfiguration(TypedDict):
    backup_configuration: NotRequired[
        "aws_sdk_observabilityadmin.types.metrics_backup_configuration.MetricsBackupConfiguration"
    ]
    """<p>Configuration defining the backup region for the metrics backup destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationMetricsConfiguration) -> dict:
    out: dict = {}
    if "backup_configuration" in value:
        import aws_sdk_observabilityadmin.types.metrics_backup_configuration

        out["BackupConfiguration"] = (
            aws_sdk_observabilityadmin.types.metrics_backup_configuration.serialize_json(
                value["backup_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DestinationMetricsConfiguration:
    out: DestinationMetricsConfiguration = {}  # type: ignore[typeddict-item]
    if "BackupConfiguration" in data:
        import aws_sdk_observabilityadmin.types.metrics_backup_configuration

        out["backup_configuration"] = (
            aws_sdk_observabilityadmin.types.metrics_backup_configuration.deserialize_json(
                data["BackupConfiguration"]
            )
        )
    return out
