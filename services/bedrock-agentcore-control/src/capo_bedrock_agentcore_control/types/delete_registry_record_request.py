"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteRegistryRecordRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.record_identifier
    import capo_bedrock_agentcore_control.types.registry_identifier


class DeleteRegistryRecordRequest(TypedDict, closed=True):
    registry_id: (
        "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier"
    )
    """<p>The identifier of the registry containing the record. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>"""
    record_id: "capo_bedrock_agentcore_control.types.record_identifier.RecordIdentifier"
    """<p>The identifier of the registry record to delete. You can specify either the Amazon Resource Name (ARN) or the ID of the record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRegistryRecordRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRegistryRecordRequest:
    out: DeleteRegistryRecordRequest = {}  # type: ignore[typeddict-item]
    return out
