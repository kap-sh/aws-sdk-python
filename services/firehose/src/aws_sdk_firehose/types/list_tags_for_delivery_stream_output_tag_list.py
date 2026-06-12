"""Generated from Smithy shape ``com.amazonaws.firehose#ListTagsForDeliveryStreamOutputTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_firehose.types.tag

ListTagsForDeliveryStreamOutputTagList: TypeAlias = list[
    "aws_sdk_firehose.types.tag.Tag"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForDeliveryStreamOutputTagList) -> list:
    import aws_sdk_firehose.types.tag

    out: list = []
    for item in value:
        out.append(aws_sdk_firehose.types.tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListTagsForDeliveryStreamOutputTagList:
    import aws_sdk_firehose.types.tag

    out: ListTagsForDeliveryStreamOutputTagList = []
    for item in data:
        out.append(aws_sdk_firehose.types.tag.deserialize_aws_json_1_1(item))
    return out
