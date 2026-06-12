"""Generated from Smithy shape ``com.amazonaws.firehose#ListDeliveryStreamsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_firehose.types.boolean_object
    import aws_sdk_firehose.types.delivery_stream_name_list


class ListDeliveryStreamsOutput(TypedDict):
    delivery_stream_names: (
        "aws_sdk_firehose.types.delivery_stream_name_list.DeliveryStreamNameList"
    )
    """<p>The names of the Firehose streams.</p>"""
    has_more_delivery_streams: "aws_sdk_firehose.types.boolean_object.BooleanObject"
    """<p>Indicates whether there are more Firehose streams available to list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDeliveryStreamsOutput) -> dict:
    out: dict = {}
    import aws_sdk_firehose.types.delivery_stream_name_list

    out["DeliveryStreamNames"] = (
        aws_sdk_firehose.types.delivery_stream_name_list.serialize_aws_json_1_1(
            value["delivery_stream_names"]
        )
    )
    out["HasMoreDeliveryStreams"] = value["has_more_delivery_streams"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDeliveryStreamsOutput:
    out: ListDeliveryStreamsOutput = {}  # type: ignore[typeddict-item]
    if "DeliveryStreamNames" in data:
        import aws_sdk_firehose.types.delivery_stream_name_list

        out["delivery_stream_names"] = (
            aws_sdk_firehose.types.delivery_stream_name_list.deserialize_aws_json_1_1(
                data["DeliveryStreamNames"]
            )
        )
    else:
        raise DeserializationError(
            "ListDeliveryStreamsOutput.delivery_stream_names required"
        )
    if "HasMoreDeliveryStreams" in data:
        out["has_more_delivery_streams"] = data["HasMoreDeliveryStreams"]
    else:
        raise DeserializationError(
            "ListDeliveryStreamsOutput.has_more_delivery_streams required"
        )
    return out
