"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#MigrationWorkflowSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_migrationhuborchestrator.types.migration_workflow_id
    import capo_migrationhuborchestrator.types.migration_workflow_status_enum


class MigrationWorkflowSummary(TypedDict, closed=True):
    id: NotRequired[
        "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    ]
    """<p>The ID of the migration workflow.</p>"""
    name: NotRequired["str"]
    """<p>The name of the migration workflow.</p>"""
    template_id: NotRequired["str"]
    """<p>The ID of the template.</p>"""
    ads_application_configuration_name: NotRequired["str"]
    """<p>The name of the application configured in Application Discovery Service.</p>"""
    status: NotRequired[
        "capo_migrationhuborchestrator.types.migration_workflow_status_enum.MigrationWorkflowStatusEnum"
    ]
    """<p>The status of the migration workflow.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>The time at which the migration workflow was created.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The time at which the migration workflow ended.</p>"""
    status_message: NotRequired["str"]
    """<p>The status message of the migration workflow.</p>"""
    completed_steps: NotRequired["int"]
    """<p>The steps completed in the migration workflow.</p>"""
    total_steps: NotRequired["int"]
    """<p>All the steps in a migration workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MigrationWorkflowSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "template_id" in value:
        out["templateId"] = value["template_id"]
    if "ads_application_configuration_name" in value:
        out["adsApplicationConfigurationName"] = value[
            "ads_application_configuration_name"
        ]
    if "status" in value:
        out["status"] = value["status"]
    if "creation_time" in value:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["creationTime"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "end_time" in value:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["endTime"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["end_time"]
            )
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "completed_steps" in value:
        out["completedSteps"] = value["completed_steps"]
    if "total_steps" in value:
        out["totalSteps"] = value["total_steps"]
    return out


def deserialize_json(data: dict) -> MigrationWorkflowSummary:
    out: MigrationWorkflowSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "templateId" in data:
        out["template_id"] = data["templateId"]
    if "adsApplicationConfigurationName" in data:
        out["ads_application_configuration_name"] = data[
            "adsApplicationConfigurationName"
        ]
    if "status" in data:
        out["status"] = data["status"]
    if "creationTime" in data:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["creation_time"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    if "endTime" in data:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["end_time"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "completedSteps" in data:
        out["completed_steps"] = data["completedSteps"]
    if "totalSteps" in data:
        out["total_steps"] = data["totalSteps"]
    return out
