"""Generated from Smithy shape ``com.amazonaws.mgn#SourceServerActionDocuments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.source_server_action_document

SourceServerActionDocuments: TypeAlias = list[
    "capo_mgn.types.source_server_action_document.SourceServerActionDocument"
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceServerActionDocuments) -> list:
    import capo_mgn.types.source_server_action_document

    out: list = []
    for item in value:
        out.append(capo_mgn.types.source_server_action_document.serialize_json(item))
    return out


def deserialize_json(data: list) -> SourceServerActionDocuments:
    import capo_mgn.types.source_server_action_document

    out: SourceServerActionDocuments = []
    for item in data:
        out.append(capo_mgn.types.source_server_action_document.deserialize_json(item))
    return out
