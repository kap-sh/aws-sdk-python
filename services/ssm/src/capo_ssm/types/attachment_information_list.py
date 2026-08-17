"""Generated from Smithy shape ``com.amazonaws.ssm#AttachmentInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.attachment_information

AttachmentInformationList: TypeAlias = list[
    "capo_ssm.types.attachment_information.AttachmentInformation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachmentInformationList) -> list:
    import capo_ssm.types.attachment_information

    out: list = []
    for item in value:
        out.append(capo_ssm.types.attachment_information.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AttachmentInformationList:
    import capo_ssm.types.attachment_information

    out: AttachmentInformationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.attachment_information.deserialize_aws_json_1_1(item))
    return out
