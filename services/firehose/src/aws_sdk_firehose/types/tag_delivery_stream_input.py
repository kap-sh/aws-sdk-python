"""Generated from Smithy shape ``com.amazonaws.firehose#TagDeliveryStreamInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_firehose.types.delivery_stream_name
    import aws_sdk_firehose.types.tag_delivery_stream_input_tag_list


class TagDeliveryStreamInput(TypedDict):
    delivery_stream_name: (
        "aws_sdk_firehose.types.delivery_stream_name.DeliveryStreamName"
    )
    """<p>The name of the Firehose stream to which you want to add the tags.</p>"""
    tags: "aws_sdk_firehose.types.tag_delivery_stream_input_tag_list.TagDeliveryStreamInputTagList"
    """<p>A set of key-value pairs to use to create the tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagDeliveryStreamInput) -> dict:
    out: dict = {}
    out["DeliveryStreamName"] = value["delivery_stream_name"]
    import aws_sdk_firehose.types.tag_delivery_stream_input_tag_list

    out["Tags"] = (
        aws_sdk_firehose.types.tag_delivery_stream_input_tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagDeliveryStreamInput:
    out: TagDeliveryStreamInput = {}  # type: ignore[typeddict-item]
    if "DeliveryStreamName" in data:
        out["delivery_stream_name"] = data["DeliveryStreamName"]
    else:
        raise DeserializationError(
            "TagDeliveryStreamInput.delivery_stream_name required"
        )
    if "Tags" in data:
        import aws_sdk_firehose.types.tag_delivery_stream_input_tag_list

        out["tags"] = (
            aws_sdk_firehose.types.tag_delivery_stream_input_tag_list.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    else:
        raise DeserializationError("TagDeliveryStreamInput.tags required")
    return out
