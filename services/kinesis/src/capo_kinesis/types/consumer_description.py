"""Generated from Smithy shape ``com.amazonaws.kinesis#ConsumerDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.consumer_arn
    import capo_kinesis.types.consumer_name
    import capo_kinesis.types.consumer_status
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.timestamp


class ConsumerDescription(TypedDict, closed=True):
    consumer_name: "capo_kinesis.types.consumer_name.ConsumerName"
    """<p>The name of the consumer is something you choose when you register the consumer.</p>"""
    consumer_arn: "capo_kinesis.types.consumer_arn.ConsumerARN"
    """<p>When you register a consumer, Kinesis Data Streams generates an ARN for it. You need this ARN to be able to call <a>SubscribeToShard</a>.</p> <p>If you delete a consumer and then create a new one with the same name, it won't have the same ARN. That's because consumer ARNs contain the creation timestamp. This is important to keep in mind if you have IAM policies that reference consumer ARNs.</p>"""
    consumer_status: "capo_kinesis.types.consumer_status.ConsumerStatus"
    """<p>A consumer can't read data while in the <code>CREATING</code> or <code>DELETING</code> states.</p>"""
    consumer_creation_timestamp: "capo_kinesis.types.timestamp.Timestamp"
    """<p></p>"""
    stream_arn: "capo_kinesis.types.stream_arn.StreamARN"
    """<p>The ARN of the stream with which you registered the consumer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConsumerDescription) -> dict:
    out: dict = {}
    out["ConsumerName"] = value["consumer_name"]
    out["ConsumerARN"] = value["consumer_arn"]
    import capo_kinesis.types.consumer_status

    out["ConsumerStatus"] = capo_kinesis.types.consumer_status.serialize_aws_json_1_1(
        value["consumer_status"]
    )
    import capo_kinesis.types.timestamp

    out["ConsumerCreationTimestamp"] = (
        capo_kinesis.types.timestamp.serialize_aws_json_1_1(
            value["consumer_creation_timestamp"]
        )
    )
    out["StreamARN"] = value["stream_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConsumerDescription:
    out: ConsumerDescription = {}  # type: ignore[typeddict-item]
    if "ConsumerName" in data:
        out["consumer_name"] = data["ConsumerName"]
    else:
        raise DeserializationError("ConsumerDescription.consumer_name required")
    if "ConsumerARN" in data:
        out["consumer_arn"] = data["ConsumerARN"]
    else:
        raise DeserializationError("ConsumerDescription.consumer_arn required")
    if "ConsumerStatus" in data:
        import capo_kinesis.types.consumer_status

        out["consumer_status"] = (
            capo_kinesis.types.consumer_status.deserialize_aws_json_1_1(
                data["ConsumerStatus"]
            )
        )
    else:
        raise DeserializationError("ConsumerDescription.consumer_status required")
    if "ConsumerCreationTimestamp" in data:
        import capo_kinesis.types.timestamp

        out["consumer_creation_timestamp"] = (
            capo_kinesis.types.timestamp.deserialize_aws_json_1_1(
                data["ConsumerCreationTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "ConsumerDescription.consumer_creation_timestamp required"
        )
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    else:
        raise DeserializationError("ConsumerDescription.stream_arn required")
    return out
