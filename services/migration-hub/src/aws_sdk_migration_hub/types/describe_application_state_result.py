"""Generated from Smithy shape ``com.amazonaws.migrationhub#DescribeApplicationStateResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.application_status
    import aws_sdk_migration_hub.types.update_date_time


class DescribeApplicationStateResult(TypedDict):
    application_status: NotRequired[
        "aws_sdk_migration_hub.types.application_status.ApplicationStatus"
    ]
    """<p>Status of the application - Not Started, In-Progress, Complete.</p>"""
    last_updated_time: NotRequired[
        "aws_sdk_migration_hub.types.update_date_time.UpdateDateTime"
    ]
    """<p>The timestamp when the application status was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationStateResult) -> dict:
    out: dict = {}
    if "application_status" in value:
        import aws_sdk_migration_hub.types.application_status

        out["ApplicationStatus"] = (
            aws_sdk_migration_hub.types.application_status.serialize_aws_json_1_1(
                value["application_status"]
            )
        )
    if "last_updated_time" in value:
        import aws_sdk_migration_hub.types.update_date_time

        out["LastUpdatedTime"] = (
            aws_sdk_migration_hub.types.update_date_time.serialize_aws_json_1_1(
                value["last_updated_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationStateResult:
    out: DescribeApplicationStateResult = {}  # type: ignore[typeddict-item]
    if "ApplicationStatus" in data:
        import aws_sdk_migration_hub.types.application_status

        out["application_status"] = (
            aws_sdk_migration_hub.types.application_status.deserialize_aws_json_1_1(
                data["ApplicationStatus"]
            )
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_migration_hub.types.update_date_time

        out["last_updated_time"] = (
            aws_sdk_migration_hub.types.update_date_time.deserialize_aws_json_1_1(
                data["LastUpdatedTime"]
            )
        )
    return out
