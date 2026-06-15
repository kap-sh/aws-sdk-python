"""Generated from Smithy shape ``com.amazonaws.iot#FirehoseAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.aws_arn
    import aws_sdk_iot.types.batch_mode
    import aws_sdk_iot.types.delivery_stream_name
    import aws_sdk_iot.types.firehose_separator


class FirehoseAction(TypedDict):
    role_arn: "aws_sdk_iot.types.aws_arn.AwsArn"
    """<p>The IAM role that grants access to the Amazon Kinesis Firehose stream.</p>"""
    delivery_stream_name: "aws_sdk_iot.types.delivery_stream_name.DeliveryStreamName"
    """<p>The delivery stream name.</p>"""
    separator: NotRequired["aws_sdk_iot.types.firehose_separator.FirehoseSeparator"]
    r"""<p>A character separator that will be used to separate records written to the Firehose stream. Valid values are: '\n' (newline), '\t' (tab), '\r\n' (Windows newline), ',' (comma).</p>"""
    batch_mode: NotRequired["aws_sdk_iot.types.batch_mode.BatchMode"]
    r"""<p>Whether to deliver the Kinesis Data Firehose stream as a batch by using <a href=\"https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch.html\"> <code>PutRecordBatch</code> </a>. The default value is <code>false</code>.</p> <p>When <code>batchMode</code> is <code>true</code> and the rule's SQL statement evaluates to an Array, each Array element forms one record in the <a href=\"https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch.html\"> <code>PutRecordBatch</code> </a> request. The resulting array can't have more than 500 records.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FirehoseAction) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["deliveryStreamName"] = value["delivery_stream_name"]
    if "separator" in value:
        out["separator"] = value["separator"]
    if "batch_mode" in value:
        out["batchMode"] = value["batch_mode"]
    return out


def deserialize_json(data: dict) -> FirehoseAction:
    out: FirehoseAction = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("FirehoseAction.role_arn required")
    if "deliveryStreamName" in data:
        out["delivery_stream_name"] = data["deliveryStreamName"]
    else:
        raise DeserializationError("FirehoseAction.delivery_stream_name required")
    if "separator" in data:
        out["separator"] = data["separator"]
    if "batchMode" in data:
        out["batch_mode"] = data["batchMode"]
    return out
