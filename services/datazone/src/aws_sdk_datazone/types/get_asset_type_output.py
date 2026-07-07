"""Generated from Smithy shape ``com.amazonaws.datazone#GetAssetTypeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.forms_output_map
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.revision
    import aws_sdk_datazone.types.type_name
    import aws_sdk_datazone.types.updated_at
    import aws_sdk_datazone.types.updated_by


class GetAssetTypeOutput(TypedDict, closed=True):
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the asset type exists.</p>"""
    name: "aws_sdk_datazone.types.type_name.TypeName"
    """<p>The name of the asset type.</p>"""
    revision: "aws_sdk_datazone.types.revision.Revision"
    """<p>The revision of the asset type.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the asset type.</p>"""
    forms_output: "aws_sdk_datazone.types.forms_output_map.FormsOutputMap"
    """<p>The metadata forms attached to the asset type.</p>"""
    owning_project_id: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The ID of the Amazon DataZone project that owns the asset type.</p>"""
    origin_domain_id: NotRequired["aws_sdk_datazone.types.domain_id.DomainId"]
    """<p>The ID of the Amazon DataZone domain in which the asset type was originally created.</p>"""
    origin_project_id: NotRequired["aws_sdk_datazone.types.project_id.ProjectId"]
    """<p>The ID of the Amazon DataZone project in which the asset type was originally created.</p>"""
    created_at: NotRequired["aws_sdk_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the asset type was created.</p>"""
    created_by: NotRequired["aws_sdk_datazone.types.created_by.CreatedBy"]
    """<p>The Amazon DataZone user who created the asset type.</p>"""
    updated_at: NotRequired["aws_sdk_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp of when the asset type was updated.</p>"""
    updated_by: NotRequired["aws_sdk_datazone.types.updated_by.UpdatedBy"]
    """<p>The Amazon DataZone user that updated the asset type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssetTypeOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["name"] = value["name"]
    out["revision"] = value["revision"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_datazone.types.forms_output_map

    out["formsOutput"] = aws_sdk_datazone.types.forms_output_map.serialize_json(
        value["forms_output"]
    )
    out["owningProjectId"] = value["owning_project_id"]
    if "origin_domain_id" in value:
        out["originDomainId"] = value["origin_domain_id"]
    if "origin_project_id" in value:
        out["originProjectId"] = value["origin_project_id"]
    if "created_at" in value:
        import aws_sdk_datazone.types.created_at

        out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import aws_sdk_datazone.types.updated_at

        out["updatedAt"] = aws_sdk_datazone.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    return out


def deserialize_json(data: dict) -> GetAssetTypeOutput:
    out: GetAssetTypeOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("GetAssetTypeOutput.domain_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetAssetTypeOutput.name required")
    if "revision" in data:
        out["revision"] = data["revision"]
    else:
        raise DeserializationError("GetAssetTypeOutput.revision required")
    if "description" in data:
        out["description"] = data["description"]
    if "formsOutput" in data:
        import aws_sdk_datazone.types.forms_output_map

        out["forms_output"] = aws_sdk_datazone.types.forms_output_map.deserialize_json(
            data["formsOutput"]
        )
    else:
        raise DeserializationError("GetAssetTypeOutput.forms_output required")
    if "owningProjectId" in data:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        raise DeserializationError("GetAssetTypeOutput.owning_project_id required")
    if "originDomainId" in data:
        out["origin_domain_id"] = data["originDomainId"]
    if "originProjectId" in data:
        out["origin_project_id"] = data["originProjectId"]
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "updatedAt" in data:
        import aws_sdk_datazone.types.updated_at

        out["updated_at"] = aws_sdk_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    return out
