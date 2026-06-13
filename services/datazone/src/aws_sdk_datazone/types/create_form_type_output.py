"""Generated from Smithy shape ``com.amazonaws.datazone#CreateFormTypeOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.form_type_name
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.revision


class CreateFormTypeOutput(TypedDict):
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which this metadata form type is created.</p>"""
    name: "aws_sdk_datazone.types.form_type_name.FormTypeName"
    """<p>The name of this Amazon DataZone metadata form type.</p>"""
    revision: "aws_sdk_datazone.types.revision.Revision"
    """<p>The revision of this Amazon DataZone metadata form type.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of this Amazon DataZone metadata form type.</p>"""
    owning_project_id: NotRequired["aws_sdk_datazone.types.project_id.ProjectId"]
    """<p>The ID of the project that owns this Amazon DataZone metadata form type.</p>"""
    origin_domain_id: NotRequired["aws_sdk_datazone.types.domain_id.DomainId"]
    """<p>The ID of the Amazon DataZone domain in which this metadata form type was originally created.</p>"""
    origin_project_id: NotRequired["aws_sdk_datazone.types.project_id.ProjectId"]
    """<p>The ID of the project in which this Amazon DataZone metadata form type was originally created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFormTypeOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["name"] = value["name"]
    out["revision"] = value["revision"]
    if "description" in value:
        out["description"] = value["description"]
    if "owning_project_id" in value:
        out["owningProjectId"] = value["owning_project_id"]
    if "origin_domain_id" in value:
        out["originDomainId"] = value["origin_domain_id"]
    if "origin_project_id" in value:
        out["originProjectId"] = value["origin_project_id"]
    return out


def deserialize_json(data: dict) -> CreateFormTypeOutput:
    out: CreateFormTypeOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("CreateFormTypeOutput.domain_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateFormTypeOutput.name required")
    if "revision" in data:
        out["revision"] = data["revision"]
    else:
        raise DeserializationError("CreateFormTypeOutput.revision required")
    if "description" in data:
        out["description"] = data["description"]
    if "owningProjectId" in data:
        out["owning_project_id"] = data["owningProjectId"]
    if "originDomainId" in data:
        out["origin_domain_id"] = data["originDomainId"]
    if "originProjectId" in data:
        out["origin_project_id"] = data["originProjectId"]
    return out
