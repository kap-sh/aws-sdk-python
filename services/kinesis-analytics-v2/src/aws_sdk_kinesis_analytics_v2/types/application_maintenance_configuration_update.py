"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationMaintenanceConfigurationUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_maintenance_window_start_time


class ApplicationMaintenanceConfigurationUpdate(TypedDict):
    application_maintenance_window_start_time_update: "aws_sdk_kinesis_analytics_v2.types.application_maintenance_window_start_time.ApplicationMaintenanceWindowStartTime"
    """<p>The updated start time for the maintenance window.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationMaintenanceConfigurationUpdate) -> dict:
    out: dict = {}
    out["ApplicationMaintenanceWindowStartTimeUpdate"] = value[
        "application_maintenance_window_start_time_update"
    ]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationMaintenanceConfigurationUpdate:
    out: ApplicationMaintenanceConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if "ApplicationMaintenanceWindowStartTimeUpdate" in data:
        out["application_maintenance_window_start_time_update"] = data[
            "ApplicationMaintenanceWindowStartTimeUpdate"
        ]
    else:
        raise DeserializationError(
            "ApplicationMaintenanceConfigurationUpdate.application_maintenance_window_start_time_update required"
        )
    return out
