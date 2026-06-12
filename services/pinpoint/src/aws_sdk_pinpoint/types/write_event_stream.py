"""Generated from Smithy shape ``com.amazonaws.pinpoint#WriteEventStream``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class WriteEventStream(TypedDict):
    destination_stream_arn: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Kinesis data stream or Amazon Kinesis Data Firehose delivery stream that you want to publish event data to.</p> <p>For a Kinesis data stream, the ARN format is: arn:aws:kinesis:<replaceable>region</replaceable>:<replaceable>account-id</replaceable>:stream/<replaceable>stream_name</replaceable> </p> <p>For a Kinesis Data Firehose delivery stream, the ARN format is: arn:aws:firehose:<replaceable>region</replaceable>:<replaceable>account-id</replaceable>:deliverystream/<replaceable>stream_name</replaceable> </p>"""
    role_arn: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The AWS Identity and Access Management (IAM) role that authorizes Amazon Pinpoint to publish event data to the stream in your AWS account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WriteEventStream) -> dict:
    out: dict = {}
    if "destination_stream_arn" in value:
        out["DestinationStreamArn"] = value["destination_stream_arn"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> WriteEventStream:
    out: WriteEventStream = {}  # type: ignore[typeddict-item]
    if "DestinationStreamArn" in data:
        out["destination_stream_arn"] = data["DestinationStreamArn"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
