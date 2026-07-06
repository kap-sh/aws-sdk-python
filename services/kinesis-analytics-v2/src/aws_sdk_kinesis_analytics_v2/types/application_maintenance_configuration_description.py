"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationMaintenanceConfigurationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_maintenance_window_end_time
    import aws_sdk_kinesis_analytics_v2.types.application_maintenance_window_start_time


class ApplicationMaintenanceConfigurationDescription(TypedDict, closed=True):
    application_maintenance_window_start_time: "aws_sdk_kinesis_analytics_v2.types.application_maintenance_window_start_time.ApplicationMaintenanceWindowStartTime"
    """<p>The start time for the maintenance window.</p>"""
    application_maintenance_window_end_time: "aws_sdk_kinesis_analytics_v2.types.application_maintenance_window_end_time.ApplicationMaintenanceWindowEndTime"
    """<p>The end time for the maintenance window.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ApplicationMaintenanceConfigurationDescription,
) -> dict:
    out: dict = {}
    out["ApplicationMaintenanceWindowStartTime"] = value[
        "application_maintenance_window_start_time"
    ]
    out["ApplicationMaintenanceWindowEndTime"] = value[
        "application_maintenance_window_end_time"
    ]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ApplicationMaintenanceConfigurationDescription:
    out: ApplicationMaintenanceConfigurationDescription = {}  # type: ignore[typeddict-item]
    if "ApplicationMaintenanceWindowStartTime" in data:
        out["application_maintenance_window_start_time"] = data[
            "ApplicationMaintenanceWindowStartTime"
        ]
    else:
        raise DeserializationError(
            "ApplicationMaintenanceConfigurationDescription.application_maintenance_window_start_time required"
        )
    if "ApplicationMaintenanceWindowEndTime" in data:
        out["application_maintenance_window_end_time"] = data[
            "ApplicationMaintenanceWindowEndTime"
        ]
    else:
        raise DeserializationError(
            "ApplicationMaintenanceConfigurationDescription.application_maintenance_window_end_time required"
        )
    return out
