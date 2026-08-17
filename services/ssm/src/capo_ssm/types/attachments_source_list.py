"""Generated from Smithy shape ``com.amazonaws.ssm#AttachmentsSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.attachments_source

AttachmentsSourceList: TypeAlias = list[
    "capo_ssm.types.attachments_source.AttachmentsSource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachmentsSourceList) -> list:
    import capo_ssm.types.attachments_source

    out: list = []
    for item in value:
        out.append(capo_ssm.types.attachments_source.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AttachmentsSourceList:
    import capo_ssm.types.attachments_source

    out: AttachmentsSourceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.attachments_source.deserialize_aws_json_1_1(item))
    return out
