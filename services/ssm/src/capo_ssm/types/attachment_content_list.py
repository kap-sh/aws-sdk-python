"""Generated from Smithy shape ``com.amazonaws.ssm#AttachmentContentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.attachment_content

AttachmentContentList: TypeAlias = list[
    "capo_ssm.types.attachment_content.AttachmentContent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachmentContentList) -> list:
    import capo_ssm.types.attachment_content

    out: list = []
    for item in value:
        out.append(capo_ssm.types.attachment_content.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AttachmentContentList:
    import capo_ssm.types.attachment_content

    out: AttachmentContentList = []
    for item in data:
        out.append(capo_ssm.types.attachment_content.deserialize_aws_json_1_1(item))
    return out
