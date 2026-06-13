"""Generated from Smithy shape ``com.amazonaws.datazone#CancelMetadataGenerationRunInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.metadata_generation_run_identifier


class CancelMetadataGenerationRunInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the metadata generation run is to be cancelled.</p>"""
    identifier: "aws_sdk_datazone.types.metadata_generation_run_identifier.MetadataGenerationRunIdentifier"
    """<p>The ID of the metadata generation run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelMetadataGenerationRunInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelMetadataGenerationRunInput:
    out: CancelMetadataGenerationRunInput = {}  # type: ignore[typeddict-item]
    return out
