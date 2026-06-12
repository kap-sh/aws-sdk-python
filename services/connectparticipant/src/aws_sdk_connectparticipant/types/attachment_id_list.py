"""Generated from Smithy shape ``com.amazonaws.connectparticipant#AttachmentIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.artifact_id

AttachmentIdList: TypeAlias = list[
    "aws_sdk_connectparticipant.types.artifact_id.ArtifactId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AttachmentIdList:
    return list(data)
