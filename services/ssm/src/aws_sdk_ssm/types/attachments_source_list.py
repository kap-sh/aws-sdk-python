"""Generated from Smithy shape ``com.amazonaws.ssm#AttachmentsSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.attachments_source

AttachmentsSourceList: TypeAlias = list[
    "aws_sdk_ssm.types.attachments_source.AttachmentsSource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachmentsSourceList) -> list:
    import aws_sdk_ssm.types.attachments_source

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.attachments_source.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AttachmentsSourceList:
    import aws_sdk_ssm.types.attachments_source

    out: AttachmentsSourceList = []
    for item in data:
        out.append(aws_sdk_ssm.types.attachments_source.deserialize_aws_json_1_1(item))
    return out
