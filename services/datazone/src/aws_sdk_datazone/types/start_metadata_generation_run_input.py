"""Generated from Smithy shape ``com.amazonaws.datazone#StartMetadataGenerationRunInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.metadata_generation_run_target
    import aws_sdk_datazone.types.metadata_generation_run_type
    import aws_sdk_datazone.types.metadata_generation_run_types
    import aws_sdk_datazone.types.project_id


class StartMetadataGenerationRunInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain where you want to start a metadata generation run.</p>"""
    type: NotRequired[
        "aws_sdk_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
    ]
    """<p>The type of the metadata generation run.</p>"""
    types: NotRequired[
        "aws_sdk_datazone.types.metadata_generation_run_types.MetadataGenerationRunTypes"
    ]
    """<p>The types of the metadata generation run.</p>"""
    target: "aws_sdk_datazone.types.metadata_generation_run_target.MetadataGenerationRunTarget"
    """<p>The asset for which you want to start a metadata generation run.</p>"""
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>"""
    owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The ID of the project that owns the asset for which you want to start a metadata generation run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMetadataGenerationRunInput) -> dict:
    out: dict = {}
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
    import aws_sdk_datazone.types.metadata_generation_run_target

    out["target"] = (
        aws_sdk_datazone.types.metadata_generation_run_target.serialize_json(
            value["target"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["owningProjectIdentifier"] = value["owning_project_identifier"]
    return out


def deserialize_json(data: dict) -> StartMetadataGenerationRunInput:
    out: StartMetadataGenerationRunInput = {}  # type: ignore[typeddict-item]
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
    if "target" in data:
        import aws_sdk_datazone.types.metadata_generation_run_target

        out["target"] = (
            aws_sdk_datazone.types.metadata_generation_run_target.deserialize_json(
                data["target"]
            )
        )
    else:
        raise DeserializationError("StartMetadataGenerationRunInput.target required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "owningProjectIdentifier" in data:
        out["owning_project_identifier"] = data["owningProjectIdentifier"]
    else:
        raise DeserializationError(
            "StartMetadataGenerationRunInput.owning_project_identifier required"
        )
    return out
