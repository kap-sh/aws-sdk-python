"""Generated from Smithy shape ``com.amazonaws.firehose#UntagDeliveryStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.delivery_stream_name
    import capo_firehose.types.tag_key_list


class UntagDeliveryStreamInput(TypedDict, closed=True):
    delivery_stream_name: "capo_firehose.types.delivery_stream_name.DeliveryStreamName"
    """<p>The name of the Firehose stream.</p>"""
    tag_keys: "capo_firehose.types.tag_key_list.TagKeyList"
    """<p>A list of tag keys. Each corresponding tag is removed from the delivery stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagDeliveryStreamInput) -> dict:
    out: dict = {}
    out["DeliveryStreamName"] = value["delivery_stream_name"]
    import capo_firehose.types.tag_key_list

    out["TagKeys"] = capo_firehose.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagDeliveryStreamInput:
    out: UntagDeliveryStreamInput = {}  # type: ignore[typeddict-item]
    if "DeliveryStreamName" in data:
        out["delivery_stream_name"] = data["DeliveryStreamName"]
    else:
        raise DeserializationError(
            "UntagDeliveryStreamInput.delivery_stream_name required"
        )
    if "TagKeys" in data:
        import capo_firehose.types.tag_key_list

        out["tag_keys"] = capo_firehose.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("UntagDeliveryStreamInput.tag_keys required")
    return out
