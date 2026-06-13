"""Generated from Smithy shape ``com.amazonaws.mgn#SourceServerActionDocuments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.source_server_action_document

SourceServerActionDocuments: TypeAlias = list[
    "aws_sdk_mgn.types.source_server_action_document.SourceServerActionDocument"
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceServerActionDocuments) -> list:
    import aws_sdk_mgn.types.source_server_action_document

    out: list = []
    for item in value:
        out.append(aws_sdk_mgn.types.source_server_action_document.serialize_json(item))
    return out


def deserialize_json(data: list) -> SourceServerActionDocuments:
    import aws_sdk_mgn.types.source_server_action_document

    out: SourceServerActionDocuments = []
    for item in data:
        out.append(
            aws_sdk_mgn.types.source_server_action_document.deserialize_json(item)
        )
    return out
