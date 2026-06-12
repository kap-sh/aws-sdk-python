"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterDeferredMaintenanceWindow``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsRedshiftClusterDeferredMaintenanceWindow(TypedDict):
    defer_maintenance_end_time: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The end of the time window for which maintenance was deferred.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    defer_maintenance_identifier: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the maintenance window.</p>"""
    defer_maintenance_start_time: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The start of the time window for which maintenance was deferred.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterDeferredMaintenanceWindow) -> dict:
    out: dict = {}
    if "defer_maintenance_end_time" in value:
        out["DeferMaintenanceEndTime"] = value["defer_maintenance_end_time"]
    if "defer_maintenance_identifier" in value:
        out["DeferMaintenanceIdentifier"] = value["defer_maintenance_identifier"]
    if "defer_maintenance_start_time" in value:
        out["DeferMaintenanceStartTime"] = value["defer_maintenance_start_time"]
    return out


def deserialize_json(data: dict) -> AwsRedshiftClusterDeferredMaintenanceWindow:
    out: AwsRedshiftClusterDeferredMaintenanceWindow = {}  # type: ignore[typeddict-item]
    if "DeferMaintenanceEndTime" in data:
        out["defer_maintenance_end_time"] = data["DeferMaintenanceEndTime"]
    if "DeferMaintenanceIdentifier" in data:
        out["defer_maintenance_identifier"] = data["DeferMaintenanceIdentifier"]
    if "DeferMaintenanceStartTime" in data:
        out["defer_maintenance_start_time"] = data["DeferMaintenanceStartTime"]
    return out
