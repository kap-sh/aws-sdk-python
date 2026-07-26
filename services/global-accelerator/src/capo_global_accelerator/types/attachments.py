"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#Attachments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_global_accelerator.types.attachment

Attachments: TypeAlias = list["capo_global_accelerator.types.attachment.Attachment"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Attachments) -> list:
    import capo_global_accelerator.types.attachment

    out: list = []
    for item in value:
        out.append(
            capo_global_accelerator.types.attachment.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Attachments:
    import capo_global_accelerator.types.attachment

    out: Attachments = []
    for item in data:
        out.append(
            capo_global_accelerator.types.attachment.deserialize_aws_json_1_1(item)
        )
    return out
