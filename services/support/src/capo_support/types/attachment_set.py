"""Generated from Smithy shape ``com.amazonaws.support#AttachmentSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_support.types.attachment_details

AttachmentSet: TypeAlias = list[
    "capo_support.types.attachment_details.AttachmentDetails"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachmentSet) -> list:
    import capo_support.types.attachment_details

    out: list = []
    for item in value:
        out.append(capo_support.types.attachment_details.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AttachmentSet:
    import capo_support.types.attachment_details

    out: AttachmentSet = []
    for item in data:
        out.append(capo_support.types.attachment_details.deserialize_aws_json_1_1(item))
    return out
