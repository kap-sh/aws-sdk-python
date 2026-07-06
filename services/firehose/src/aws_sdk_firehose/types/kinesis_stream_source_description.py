"""Generated from Smithy shape ``com.amazonaws.firehose#KinesisStreamSourceDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_firehose.types.delivery_start_timestamp
    import aws_sdk_firehose.types.kinesis_stream_arn
    import aws_sdk_firehose.types.role_arn


class KinesisStreamSourceDescription(TypedDict, closed=True):
    kinesis_stream_arn: NotRequired[
        "aws_sdk_firehose.types.kinesis_stream_arn.KinesisStreamARN"
    ]
    r"""<p>The Amazon Resource Name (ARN) of the source Kinesis data stream. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kinesis-streams\">Amazon Kinesis Data Streams ARN Format</a>.</p>"""
    role_arn: NotRequired["aws_sdk_firehose.types.role_arn.RoleARN"]
    r"""<p>The ARN of the role used by the source Kinesis data stream. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-iam\">Amazon Web Services Identity and Access Management (IAM) ARN Format</a>.</p>"""
    delivery_start_timestamp: NotRequired[
        "aws_sdk_firehose.types.delivery_start_timestamp.DeliveryStartTimestamp"
    ]
    """<p>Firehose starts retrieving records from the Kinesis data stream starting with this timestamp.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KinesisStreamSourceDescription) -> dict:
    out: dict = {}
    if "kinesis_stream_arn" in value:
        out["KinesisStreamARN"] = value["kinesis_stream_arn"]
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    if "delivery_start_timestamp" in value:
        import aws_sdk_firehose.types.delivery_start_timestamp

        out["DeliveryStartTimestamp"] = (
            aws_sdk_firehose.types.delivery_start_timestamp.serialize_aws_json_1_1(
                value["delivery_start_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> KinesisStreamSourceDescription:
    out: KinesisStreamSourceDescription = {}  # type: ignore[typeddict-item]
    if "KinesisStreamARN" in data:
        out["kinesis_stream_arn"] = data["KinesisStreamARN"]
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    if "DeliveryStartTimestamp" in data:
        import aws_sdk_firehose.types.delivery_start_timestamp

        out["delivery_start_timestamp"] = (
            aws_sdk_firehose.types.delivery_start_timestamp.deserialize_aws_json_1_1(
                data["DeliveryStartTimestamp"]
            )
        )
    return out
