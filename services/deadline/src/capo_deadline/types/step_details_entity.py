"""Generated from Smithy shape ``com.amazonaws.deadline#StepDetailsEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.dependencies_list
    import capo_deadline.types.document
    import capo_deadline.types.job_id
    import capo_deadline.types.step_id
    import capo_deadline.types.string


class StepDetailsEntity(TypedDict, closed=True):
    job_id: "capo_deadline.types.job_id.JobId"
    """<p>The job ID.</p>"""
    step_id: "capo_deadline.types.step_id.StepId"
    """<p>The step ID.</p>"""
    schema_version: "capo_deadline.types.string.String"
    """<p>The schema version for a step template.</p>"""
    template: "capo_deadline.types.document.Document"
    """<p>The template for a step.</p>"""
    dependencies: "capo_deadline.types.dependencies_list.DependenciesList"
    """<p>The dependencies for a step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepDetailsEntity) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["stepId"] = value["step_id"]
    out["schemaVersion"] = value["schema_version"]
    out["template"] = value["template"]
    import capo_deadline.types.dependencies_list

    out["dependencies"] = capo_deadline.types.dependencies_list.serialize_json(
        value["dependencies"]
    )
    return out


def deserialize_json(data: dict) -> StepDetailsEntity:
    out: StepDetailsEntity = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("StepDetailsEntity.job_id required")
    if "stepId" in data:
        out["step_id"] = data["stepId"]
    else:
        raise DeserializationError("StepDetailsEntity.step_id required")
    if "schemaVersion" in data:
        out["schema_version"] = data["schemaVersion"]
    else:
        raise DeserializationError("StepDetailsEntity.schema_version required")
    if "template" in data:
        out["template"] = data["template"]
    else:
        raise DeserializationError("StepDetailsEntity.template required")
    if "dependencies" in data:
        import capo_deadline.types.dependencies_list

        out["dependencies"] = capo_deadline.types.dependencies_list.deserialize_json(
            data["dependencies"]
        )
    else:
        raise DeserializationError("StepDetailsEntity.dependencies required")
    return out
