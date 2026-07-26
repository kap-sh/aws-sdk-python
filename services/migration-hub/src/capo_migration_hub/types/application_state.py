"""Generated from Smithy shape ``com.amazonaws.migrationhub#ApplicationState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub.types.application_id
    import capo_migration_hub.types.application_status
    import capo_migration_hub.types.update_date_time


class ApplicationState(TypedDict, closed=True):
    application_id: NotRequired["capo_migration_hub.types.application_id.ApplicationId"]
    """<p>The configurationId from the Application Discovery Service that uniquely identifies an application.</p>"""
    application_status: NotRequired[
        "capo_migration_hub.types.application_status.ApplicationStatus"
    ]
    """<p>The current status of an application.</p>"""
    last_updated_time: NotRequired[
        "capo_migration_hub.types.update_date_time.UpdateDateTime"
    ]
    """<p>The timestamp when the application status was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationState) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "application_status" in value:
        import capo_migration_hub.types.application_status

        out["ApplicationStatus"] = (
            capo_migration_hub.types.application_status.serialize_aws_json_1_1(
                value["application_status"]
            )
        )
    if "last_updated_time" in value:
        import capo_migration_hub.types.update_date_time

        out["LastUpdatedTime"] = (
            capo_migration_hub.types.update_date_time.serialize_aws_json_1_1(
                value["last_updated_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationState:
    out: ApplicationState = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "ApplicationStatus" in data:
        import capo_migration_hub.types.application_status

        out["application_status"] = (
            capo_migration_hub.types.application_status.deserialize_aws_json_1_1(
                data["ApplicationStatus"]
            )
        )
    if "LastUpdatedTime" in data:
        import capo_migration_hub.types.update_date_time

        out["last_updated_time"] = (
            capo_migration_hub.types.update_date_time.deserialize_aws_json_1_1(
                data["LastUpdatedTime"]
            )
        )
    return out
