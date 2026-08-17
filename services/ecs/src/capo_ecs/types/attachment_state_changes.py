"""Generated from Smithy shape ``com.amazonaws.ecs#AttachmentStateChanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.attachment_state_change

AttachmentStateChanges: TypeAlias = list[
    "capo_ecs.types.attachment_state_change.AttachmentStateChange"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachmentStateChanges) -> list:
    import capo_ecs.types.attachment_state_change

    out: list = []
    for item in value:
        out.append(capo_ecs.types.attachment_state_change.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AttachmentStateChanges:
    import capo_ecs.types.attachment_state_change

    out: AttachmentStateChanges = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.attachment_state_change.deserialize_aws_json_1_1(item)
        )
    return out
