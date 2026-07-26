"""Generated from Smithy shape ``com.amazonaws.datazone#StartMetadataGenerationRunOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.domain_id
    import capo_datazone.types.metadata_generation_run_identifier
    import capo_datazone.types.metadata_generation_run_status
    import capo_datazone.types.metadata_generation_run_type
    import capo_datazone.types.metadata_generation_run_types
    import capo_datazone.types.project_id


class StartMetadataGenerationRunOutput(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the metadata generation run was started.</p>"""
    id: "capo_datazone.types.metadata_generation_run_identifier.MetadataGenerationRunIdentifier"
    """<p>The ID of the metadata generation run.</p>"""
    status: NotRequired[
        "capo_datazone.types.metadata_generation_run_status.MetadataGenerationRunStatus"
    ]
    """<p>The status of the metadata generation run.</p>"""
    type: NotRequired[
        "capo_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
    ]
    """<p>The type of the metadata generation run.</p>"""
    types: NotRequired[
        "capo_datazone.types.metadata_generation_run_types.MetadataGenerationRunTypes"
    ]
    """<p>The types of the metadata generation run.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp at which the metadata generation run was started.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The ID of the user who started the metadata generation run.</p>"""
    owning_project_id: NotRequired["capo_datazone.types.project_id.ProjectId"]
    """<p>The ID of the project that owns the asset for which the metadata generation run was started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMetadataGenerationRunOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["id"] = value["id"]
    if "status" in value:
        import capo_datazone.types.metadata_generation_run_status

        out["status"] = (
            capo_datazone.types.metadata_generation_run_status.serialize_json(
                value["status"]
            )
        )
    if "type" in value:
        import capo_datazone.types.metadata_generation_run_type

        out["type"] = capo_datazone.types.metadata_generation_run_type.serialize_json(
            value["type"]
        )
    if "types" in value:
        import capo_datazone.types.metadata_generation_run_types

        out["types"] = capo_datazone.types.metadata_generation_run_types.serialize_json(
            value["types"]
        )
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "owning_project_id" in value:
        out["owningProjectId"] = value["owning_project_id"]
    return out


def deserialize_json(data: dict) -> StartMetadataGenerationRunOutput:
    out: StartMetadataGenerationRunOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError(
            "StartMetadataGenerationRunOutput.domain_id required"
        )
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("StartMetadataGenerationRunOutput.id required")
    if "status" in data:
        import capo_datazone.types.metadata_generation_run_status

        out["status"] = (
            capo_datazone.types.metadata_generation_run_status.deserialize_json(
                data["status"]
            )
        )
    if "type" in data:
        import capo_datazone.types.metadata_generation_run_type

        out["type"] = capo_datazone.types.metadata_generation_run_type.deserialize_json(
            data["type"]
        )
    if "types" in data:
        import capo_datazone.types.metadata_generation_run_types

        out["types"] = (
            capo_datazone.types.metadata_generation_run_types.deserialize_json(
                data["types"]
            )
        )
    if "createdAt" in data:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "owningProjectId" in data:
        out["owning_project_id"] = data["owningProjectId"]
    return out
