"""Generated from Smithy shape ``com.amazonaws.datazone#GetMetadataGenerationRunInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.metadata_generation_run_identifier
    import aws_sdk_datazone.types.metadata_generation_run_type


class GetMetadataGenerationRunInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain the metadata generation run of which you want to get.</p>"""
    identifier: "aws_sdk_datazone.types.metadata_generation_run_identifier.MetadataGenerationRunIdentifier"
    """<p>The identifier of the metadata generation run.</p>"""
    type: NotRequired[
        "aws_sdk_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
    ]
    """<p>The type of the metadata generation run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMetadataGenerationRunInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMetadataGenerationRunInput:
    out: GetMetadataGenerationRunInput = {}  # type: ignore[typeddict-item]
    return out
