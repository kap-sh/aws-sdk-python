"""Generated from Smithy shape ``com.amazonaws.datazone#GetMetadataGenerationRunInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.metadata_generation_run_identifier
    import capo_datazone.types.metadata_generation_run_type


class GetMetadataGenerationRunInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain the metadata generation run of which you want to get.</p>"""
    identifier: "capo_datazone.types.metadata_generation_run_identifier.MetadataGenerationRunIdentifier"
    """<p>The identifier of the metadata generation run.</p>"""
    type: NotRequired[
        "capo_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
    ]
    """<p>The type of the metadata generation run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMetadataGenerationRunInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMetadataGenerationRunInput:
    out: GetMetadataGenerationRunInput = {}  # type: ignore[typeddict-item]
    return out
