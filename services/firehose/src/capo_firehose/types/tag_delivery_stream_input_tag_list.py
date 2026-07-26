"""Generated from Smithy shape ``com.amazonaws.firehose#TagDeliveryStreamInputTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_firehose.types.tag

TagDeliveryStreamInputTagList: TypeAlias = list["capo_firehose.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagDeliveryStreamInputTagList) -> list:
    import capo_firehose.types.tag

    out: list = []
    for item in value:
        out.append(capo_firehose.types.tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TagDeliveryStreamInputTagList:
    import capo_firehose.types.tag

    out: TagDeliveryStreamInputTagList = []
    for item in data:
        out.append(capo_firehose.types.tag.deserialize_aws_json_1_1(item))
    return out
