"""Generated from Smithy shape ``com.amazonaws.datazone#CreateAssetTypeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.forms_output_map
    import capo_datazone.types.project_id
    import capo_datazone.types.revision
    import capo_datazone.types.type_name
    import capo_datazone.types.updated_at
    import capo_datazone.types.updated_by


class CreateAssetTypeOutput(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the asset type was created.</p>"""
    name: "capo_datazone.types.type_name.TypeName"
    """<p>The name of the asset type.</p>"""
    revision: "capo_datazone.types.revision.Revision"
    """<p>The revision of the custom asset type.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the custom asset type.</p>"""
    forms_output: "capo_datazone.types.forms_output_map.FormsOutputMap"
    """<p>The metadata forms that are attached to the asset type.</p>"""
    owning_project_id: NotRequired["capo_datazone.types.project_id.ProjectId"]
    """<p>The ID of the Amazon DataZone project that currently owns this asset type.</p>"""
    origin_domain_id: NotRequired["capo_datazone.types.domain_id.DomainId"]
    """<p>The ID of the Amazon DataZone domain where the asset type was originally created.</p>"""
    origin_project_id: NotRequired["capo_datazone.types.project_id.ProjectId"]
    """<p>The ID of the Amazon DataZone project where the asset type was originally created.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the asset type is to be created.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The Amazon DataZone user who creates this custom asset type.</p>"""
    updated_at: NotRequired["capo_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp of when the custom type was created.</p>"""
    updated_by: NotRequired["capo_datazone.types.updated_by.UpdatedBy"]
    """<p>The Amazon DataZone user that created the custom asset type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssetTypeOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["name"] = value["name"]
    out["revision"] = value["revision"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_datazone.types.forms_output_map

    out["formsOutput"] = capo_datazone.types.forms_output_map.serialize_json(
        value["forms_output"]
    )
    if "owning_project_id" in value:
        out["owningProjectId"] = value["owning_project_id"]
    if "origin_domain_id" in value:
        out["originDomainId"] = value["origin_domain_id"]
    if "origin_project_id" in value:
        out["originProjectId"] = value["origin_project_id"]
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import capo_datazone.types.updated_at

        out["updatedAt"] = capo_datazone.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    return out


def deserialize_json(data: dict) -> CreateAssetTypeOutput:
    out: CreateAssetTypeOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("CreateAssetTypeOutput.domain_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAssetTypeOutput.name required")
    if "revision" in data:
        out["revision"] = data["revision"]
    else:
        raise DeserializationError("CreateAssetTypeOutput.revision required")
    if "description" in data:
        out["description"] = data["description"]
    if "formsOutput" in data:
        import capo_datazone.types.forms_output_map

        out["forms_output"] = capo_datazone.types.forms_output_map.deserialize_json(
            data["formsOutput"]
        )
    else:
        raise DeserializationError("CreateAssetTypeOutput.forms_output required")
    if "owningProjectId" in data:
        out["owning_project_id"] = data["owningProjectId"]
    if "originDomainId" in data:
        out["origin_domain_id"] = data["originDomainId"]
    if "originProjectId" in data:
        out["origin_project_id"] = data["originProjectId"]
    if "createdAt" in data:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "updatedAt" in data:
        import capo_datazone.types.updated_at

        out["updated_at"] = capo_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    return out
