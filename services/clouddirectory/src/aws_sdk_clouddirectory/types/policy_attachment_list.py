"""Generated from Smithy shape ``com.amazonaws.clouddirectory#PolicyAttachmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.policy_attachment

PolicyAttachmentList: TypeAlias = list[
    "aws_sdk_clouddirectory.types.policy_attachment.PolicyAttachment"
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyAttachmentList) -> list:
    import aws_sdk_clouddirectory.types.policy_attachment

    out: list = []
    for item in value:
        out.append(aws_sdk_clouddirectory.types.policy_attachment.serialize_json(item))
    return out


def deserialize_json(data: list) -> PolicyAttachmentList:
    import aws_sdk_clouddirectory.types.policy_attachment

    out: PolicyAttachmentList = []
    for item in data:
        out.append(
            aws_sdk_clouddirectory.types.policy_attachment.deserialize_json(item)
        )
    return out
