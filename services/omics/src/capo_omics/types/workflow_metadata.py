"""Generated from Smithy shape ``com.amazonaws.omics#WorkflowMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.workflow_metadata_key
    import capo_omics.types.workflow_metadata_value

WorkflowMetadata: TypeAlias = dict[
    "capo_omics.types.workflow_metadata_key.WorkflowMetadataKey",
    "capo_omics.types.workflow_metadata_value.WorkflowMetadataValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: WorkflowMetadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> WorkflowMetadata:
    out: WorkflowMetadata = {}
    for key, value in data.items():
        out[key] = value
    return out
