"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.created_by
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.domain_unit_id
    import capo_datazone.types.failure_reasons
    import capo_datazone.types.project_id
    import capo_datazone.types.project_name
    import capo_datazone.types.project_status


class ProjectSummary(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of a Amazon DataZone domain where the project exists.</p>"""
    id: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of a project.</p>"""
    name: "capo_datazone.types.project_name.ProjectName"
    """<p>The name of a project.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of a project.</p>"""
    project_status: NotRequired["capo_datazone.types.project_status.ProjectStatus"]
    """<p>The status of the project.</p>"""
    failure_reasons: NotRequired["capo_datazone.types.failure_reasons.FailureReasons"]
    """<p>Specifies the error message that is returned if the operation cannot be successfully completed.</p>"""
    created_by: "capo_datazone.types.created_by.CreatedBy"
    """<p>The Amazon DataZone user who created the project.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when a project was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the project was updated.</p>"""
    domain_unit_id: NotRequired["capo_datazone.types.domain_unit_id.DomainUnitId"]
    """<p>The ID of the domain unit.</p>"""
    project_category: NotRequired["str"]
    """<p>The category of the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProjectSummary) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "project_status" in value:
        import capo_datazone.types.project_status

        out["projectStatus"] = capo_datazone.types.project_status.serialize_json(
            value["project_status"]
        )
    if "failure_reasons" in value:
        import capo_datazone.types.failure_reasons

        out["failureReasons"] = capo_datazone.types.failure_reasons.serialize_json(
            value["failure_reasons"]
        )
    out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import capo_datazone.types._prelude.timestamp

        out["createdAt"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_datazone.types._prelude.timestamp

        out["updatedAt"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "domain_unit_id" in value:
        out["domainUnitId"] = value["domain_unit_id"]
    if "project_category" in value:
        out["projectCategory"] = value["project_category"]
    return out


def deserialize_json(data: dict) -> ProjectSummary:
    out: ProjectSummary = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("ProjectSummary.domain_id required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ProjectSummary.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ProjectSummary.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "projectStatus" in data:
        import capo_datazone.types.project_status

        out["project_status"] = capo_datazone.types.project_status.deserialize_json(
            data["projectStatus"]
        )
    if "failureReasons" in data:
        import capo_datazone.types.failure_reasons

        out["failure_reasons"] = capo_datazone.types.failure_reasons.deserialize_json(
            data["failureReasons"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("ProjectSummary.created_by required")
    if "createdAt" in data:
        import capo_datazone.types._prelude.timestamp

        out["created_at"] = capo_datazone.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import capo_datazone.types._prelude.timestamp

        out["updated_at"] = capo_datazone.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "domainUnitId" in data:
        out["domain_unit_id"] = data["domainUnitId"]
    if "projectCategory" in data:
        out["project_category"] = data["projectCategory"]
    return out
