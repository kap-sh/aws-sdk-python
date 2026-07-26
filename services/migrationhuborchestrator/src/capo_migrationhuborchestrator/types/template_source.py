"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#TemplateSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_migrationhuborchestrator.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.migration_workflow_id


class _TemplateSource_workflowId(TypedDict, closed=True):
    workflowId: (
        "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    )


TemplateSource: TypeAlias = _TemplateSource_workflowId


# --- restJson1 ser/de ---
def serialize_json(value: TemplateSource) -> dict:
    if "workflowId" in value:
        return {"workflowId": value["workflowId"]}
    else:
        raise SerializationError("TemplateSource: no variant present")


def deserialize_json(data: dict) -> TemplateSource:
    if "workflowId" in data:
        return {"workflowId": data["workflowId"]}
    else:
        raise DeserializationError("TemplateSource: no recognized variant key")
