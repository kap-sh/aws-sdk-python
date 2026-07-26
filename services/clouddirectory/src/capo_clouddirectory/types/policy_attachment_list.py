"""Generated from Smithy shape ``com.amazonaws.clouddirectory#PolicyAttachmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_clouddirectory.types.policy_attachment

PolicyAttachmentList: TypeAlias = list[
    "capo_clouddirectory.types.policy_attachment.PolicyAttachment"
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyAttachmentList) -> list:
    import capo_clouddirectory.types.policy_attachment

    out: list = []
    for item in value:
        out.append(capo_clouddirectory.types.policy_attachment.serialize_json(item))
    return out


def deserialize_json(data: list) -> PolicyAttachmentList:
    import capo_clouddirectory.types.policy_attachment

    out: PolicyAttachmentList = []
    for item in data:
        out.append(capo_clouddirectory.types.policy_attachment.deserialize_json(item))
    return out
