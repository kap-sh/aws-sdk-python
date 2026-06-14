"""Generated from Smithy shape ``com.amazonaws.datazone#GetMetadataGenerationRunOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.metadata_generation_run_identifier
    import aws_sdk_datazone.types.metadata_generation_run_status
    import aws_sdk_datazone.types.metadata_generation_run_target
    import aws_sdk_datazone.types.metadata_generation_run_type
    import aws_sdk_datazone.types.metadata_generation_run_type_stats
    import aws_sdk_datazone.types.metadata_generation_run_types
    import aws_sdk_datazone.types.project_id


class GetMetadataGenerationRunOutput(TypedDict):
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain the metadata generation run of which you want to get.</p>"""
    id: "aws_sdk_datazone.types.metadata_generation_run_identifier.MetadataGenerationRunIdentifier"
    """<p>The ID of the metadata generation run.</p>"""
    target: NotRequired[
        "aws_sdk_datazone.types.metadata_generation_run_target.MetadataGenerationRunTarget"
    ]
    """<p>The asset for which you're generating metadata.</p>"""
    status: NotRequired[
        "aws_sdk_datazone.types.metadata_generation_run_status.MetadataGenerationRunStatus"
    ]
    """<p>The status of the metadata generation run.</p>"""
    type: NotRequired[
        "aws_sdk_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
    ]
    """<p>The type of metadata generation run.</p>"""
    types: NotRequired[
        "aws_sdk_datazone.types.metadata_generation_run_types.MetadataGenerationRunTypes"
    ]
    """<p>The types of the metadata generation run.</p>"""
    created_at: NotRequired["aws_sdk_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the metadata generation run was start.</p>"""
    created_by: NotRequired["aws_sdk_datazone.types.created_by.CreatedBy"]
    """<p>The Amazon DataZone user who started the metadata generation run.</p>"""
    owning_project_id: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The ID of the project that owns the assets for which you're running metadata generation.</p>"""
    type_stats: NotRequired[
        "aws_sdk_datazone.types.metadata_generation_run_type_stats.MetadataGenerationRunTypeStats"
    ]
    """<p>The type stats included in the metadata generation run output details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMetadataGenerationRunOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["id"] = value["id"]
    if "target" in value:
        import aws_sdk_datazone.types.metadata_generation_run_target

        out["target"] = (
            aws_sdk_datazone.types.metadata_generation_run_target.serialize_json(
                value["target"]
            )
        )
    if "status" in value:
        import aws_sdk_datazone.types.metadata_generation_run_status

        out["status"] = (
            aws_sdk_datazone.types.metadata_generation_run_status.serialize_json(
                value["status"]
            )
        )
    if "type" in value:
        import aws_sdk_datazone.types.metadata_generation_run_type

        out["type"] = (
            aws_sdk_datazone.types.metadata_generation_run_type.serialize_json(
                value["type"]
            )
        )
    if "types" in value:
        import aws_sdk_datazone.types.metadata_generation_run_types

        out["types"] = (
            aws_sdk_datazone.types.metadata_generation_run_types.serialize_json(
                value["types"]
            )
        )
    if "created_at" in value:
        import aws_sdk_datazone.types.created_at

        out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    out["owningProjectId"] = value["owning_project_id"]
    if "type_stats" in value:
        import aws_sdk_datazone.types.metadata_generation_run_type_stats

        out["typeStats"] = (
            aws_sdk_datazone.types.metadata_generation_run_type_stats.serialize_json(
                value["type_stats"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMetadataGenerationRunOutput:
    out: GetMetadataGenerationRunOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("GetMetadataGenerationRunOutput.domain_id required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetMetadataGenerationRunOutput.id required")
    if "target" in data:
        import aws_sdk_datazone.types.metadata_generation_run_target

        out["target"] = (
            aws_sdk_datazone.types.metadata_generation_run_target.deserialize_json(
                data["target"]
            )
        )
    if "status" in data:
        import aws_sdk_datazone.types.metadata_generation_run_status

        out["status"] = (
            aws_sdk_datazone.types.metadata_generation_run_status.deserialize_json(
                data["status"]
            )
        )
    if "type" in data:
        import aws_sdk_datazone.types.metadata_generation_run_type

        out["type"] = (
            aws_sdk_datazone.types.metadata_generation_run_type.deserialize_json(
                data["type"]
            )
        )
    if "types" in data:
        import aws_sdk_datazone.types.metadata_generation_run_types

        out["types"] = (
            aws_sdk_datazone.types.metadata_generation_run_types.deserialize_json(
                data["types"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "owningProjectId" in data:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        raise DeserializationError(
            "GetMetadataGenerationRunOutput.owning_project_id required"
        )
    if "typeStats" in data:
        import aws_sdk_datazone.types.metadata_generation_run_type_stats

        out["type_stats"] = (
            aws_sdk_datazone.types.metadata_generation_run_type_stats.deserialize_json(
                data["typeStats"]
            )
        )
    return out
