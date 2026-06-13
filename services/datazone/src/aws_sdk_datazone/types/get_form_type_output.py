"""Generated from Smithy shape ``com.amazonaws.datazone#GetFormTypeOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.form_type_name
    import aws_sdk_datazone.types.form_type_status
    import aws_sdk_datazone.types.import_list
    import aws_sdk_datazone.types.model
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.revision


class GetFormTypeOutput(TypedDict):
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which this metadata form type exists.</p>"""
    name: "aws_sdk_datazone.types.form_type_name.FormTypeName"
    """<p>The name of the metadata form type.</p>"""
    revision: "aws_sdk_datazone.types.revision.Revision"
    """<p>The revision of the metadata form type.</p>"""
    model: "aws_sdk_datazone.types.model.Model"
    """<p>The model of the metadata form type.</p>"""
    owning_project_id: NotRequired["aws_sdk_datazone.types.project_id.ProjectId"]
    """<p>The ID of the project that owns this metadata form type.</p>"""
    origin_domain_id: NotRequired["aws_sdk_datazone.types.domain_id.DomainId"]
    """<p>The ID of the Amazon DataZone domain in which the metadata form type was originally created.</p>"""
    origin_project_id: NotRequired["aws_sdk_datazone.types.project_id.ProjectId"]
    """<p>The ID of the project in which this metadata form type was originally created.</p>"""
    status: NotRequired["aws_sdk_datazone.types.form_type_status.FormTypeStatus"]
    """<p>The status of the metadata form type.</p>"""
    created_at: NotRequired["aws_sdk_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when this metadata form type was created.</p>"""
    created_by: NotRequired["aws_sdk_datazone.types.created_by.CreatedBy"]
    """<p>The Amazon DataZone user who created this metadata form type.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the metadata form type.</p>"""
    imports: NotRequired["aws_sdk_datazone.types.import_list.ImportList"]
    """<p>The imports of the metadata form type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFormTypeOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["name"] = value["name"]
    out["revision"] = value["revision"]
    import aws_sdk_datazone.types.model

    out["model"] = aws_sdk_datazone.types.model.serialize_json(value["model"])
    if "owning_project_id" in value:
        out["owningProjectId"] = value["owning_project_id"]
    if "origin_domain_id" in value:
        out["originDomainId"] = value["origin_domain_id"]
    if "origin_project_id" in value:
        out["originProjectId"] = value["origin_project_id"]
    if "status" in value:
        import aws_sdk_datazone.types.form_type_status

        out["status"] = aws_sdk_datazone.types.form_type_status.serialize_json(
            value["status"]
        )
    if "created_at" in value:
        import aws_sdk_datazone.types.created_at

        out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "description" in value:
        out["description"] = value["description"]
    if "imports" in value:
        import aws_sdk_datazone.types.import_list

        out["imports"] = aws_sdk_datazone.types.import_list.serialize_json(
            value["imports"]
        )
    return out


def deserialize_json(data: dict) -> GetFormTypeOutput:
    out: GetFormTypeOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("GetFormTypeOutput.domain_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetFormTypeOutput.name required")
    if "revision" in data:
        out["revision"] = data["revision"]
    else:
        raise DeserializationError("GetFormTypeOutput.revision required")
    if "model" in data:
        import aws_sdk_datazone.types.model

        out["model"] = aws_sdk_datazone.types.model.deserialize_json(data["model"])
    else:
        raise DeserializationError("GetFormTypeOutput.model required")
    if "owningProjectId" in data:
        out["owning_project_id"] = data["owningProjectId"]
    if "originDomainId" in data:
        out["origin_domain_id"] = data["originDomainId"]
    if "originProjectId" in data:
        out["origin_project_id"] = data["originProjectId"]
    if "status" in data:
        import aws_sdk_datazone.types.form_type_status

        out["status"] = aws_sdk_datazone.types.form_type_status.deserialize_json(
            data["status"]
        )
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "description" in data:
        out["description"] = data["description"]
    if "imports" in data:
        import aws_sdk_datazone.types.import_list

        out["imports"] = aws_sdk_datazone.types.import_list.deserialize_json(
            data["imports"]
        )
    return out
