"""Generated from Smithy shape ``com.amazonaws.deadline#QueueMemberList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.queue_member

QueueMemberList: TypeAlias = list["aws_sdk_deadline.types.queue_member.QueueMember"]


# --- restJson1 ser/de ---
def serialize_json(value: QueueMemberList) -> list:
    import aws_sdk_deadline.types.queue_member

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.queue_member.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueueMemberList:
    import aws_sdk_deadline.types.queue_member

    out: QueueMemberList = []
    for item in data:
        out.append(aws_sdk_deadline.types.queue_member.deserialize_json(item))
    return out
