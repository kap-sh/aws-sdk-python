"""Generated from Smithy shape ``com.amazonaws.deadline#QueueMemberList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.queue_member

QueueMemberList: TypeAlias = list["capo_deadline.types.queue_member.QueueMember"]


# --- restJson1 ser/de ---
def serialize_json(value: QueueMemberList) -> list:
    import capo_deadline.types.queue_member

    out: list = []
    for item in value:
        out.append(capo_deadline.types.queue_member.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueueMemberList:
    import capo_deadline.types.queue_member

    out: QueueMemberList = []
    for item in data:
        out.append(capo_deadline.types.queue_member.deserialize_json(item))
    return out
