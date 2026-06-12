"""Generated from Smithy shape ``com.amazonaws.ssm#AttachmentInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.attachment_information

AttachmentInformationList: TypeAlias = list[
    "aws_sdk_ssm.types.attachment_information.AttachmentInformation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachmentInformationList) -> list:
    import aws_sdk_ssm.types.attachment_information

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.attachment_information.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AttachmentInformationList:
    import aws_sdk_ssm.types.attachment_information

    out: AttachmentInformationList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.attachment_information.deserialize_aws_json_1_1(item)
        )
    return out
