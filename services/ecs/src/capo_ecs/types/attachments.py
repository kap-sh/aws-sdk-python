"""Generated from Smithy shape ``com.amazonaws.ecs#Attachments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.attachment

Attachments: TypeAlias = list["capo_ecs.types.attachment.Attachment"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Attachments) -> list:
    import capo_ecs.types.attachment

    out: list = []
    for item in value:
        out.append(capo_ecs.types.attachment.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Attachments:
    import capo_ecs.types.attachment

    out: Attachments = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.attachment.deserialize_aws_json_1_1(item))
    return out
