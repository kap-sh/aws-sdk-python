"""Generated from Smithy shape ``com.amazonaws.migrationhub#NotifyApplicationStateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_migration_hub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.application_id
    import aws_sdk_migration_hub.types.application_status
    import aws_sdk_migration_hub.types.dry_run
    import aws_sdk_migration_hub.types.update_date_time


class NotifyApplicationStateRequest(TypedDict):
    application_id: "aws_sdk_migration_hub.types.application_id.ApplicationId"
    """<p>The configurationId in Application Discovery Service that uniquely identifies the grouped application.</p>"""
    status: "aws_sdk_migration_hub.types.application_status.ApplicationStatus"
    """<p>Status of the application - Not Started, In-Progress, Complete.</p>"""
    update_date_time: NotRequired[
        "aws_sdk_migration_hub.types.update_date_time.UpdateDateTime"
    ]
    """<p>The timestamp when the application state changed.</p>"""
    dry_run: "aws_sdk_migration_hub.types.dry_run.DryRun"
    """<p>Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotifyApplicationStateRequest) -> dict:
    out: dict = {}
    out["ApplicationId"] = value["application_id"]
    import aws_sdk_migration_hub.types.application_status

    out["Status"] = (
        aws_sdk_migration_hub.types.application_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "update_date_time" in value:
        import aws_sdk_migration_hub.types.update_date_time

        out["UpdateDateTime"] = (
            aws_sdk_migration_hub.types.update_date_time.serialize_aws_json_1_1(
                value["update_date_time"]
            )
        )
    out["DryRun"] = value.get("dry_run", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> NotifyApplicationStateRequest:
    out: NotifyApplicationStateRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    else:
        raise DeserializationError(
            "NotifyApplicationStateRequest.application_id required"
        )
    if "Status" in data:
        import aws_sdk_migration_hub.types.application_status

        out["status"] = (
            aws_sdk_migration_hub.types.application_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("NotifyApplicationStateRequest.status required")
    if "UpdateDateTime" in data:
        import aws_sdk_migration_hub.types.update_date_time

        out["update_date_time"] = (
            aws_sdk_migration_hub.types.update_date_time.deserialize_aws_json_1_1(
                data["UpdateDateTime"]
            )
        )
    if "DryRun" in data:
        out["dry_run"] = data["DryRun"]
    else:
        out["dry_run"] = False
    return out
