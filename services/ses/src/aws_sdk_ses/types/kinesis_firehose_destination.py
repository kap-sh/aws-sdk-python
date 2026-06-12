"""Generated from Smithy shape ``com.amazonaws.ses#KinesisFirehoseDestination``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.amazon_resource_name


class KinesisFirehoseDestination(TypedDict):
    iam_role_arn: "aws_sdk_ses.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the IAM role under which Amazon SES publishes email sending events to the Amazon Kinesis Firehose stream.</p>"""
    delivery_stream_arn: "aws_sdk_ses.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the Amazon Kinesis Firehose stream that email sending events should be published to.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: KinesisFirehoseDestination, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.IAMRoleARN", str(value["iam_role_arn"])))
    pairs.append((f"{prefix}.DeliveryStreamARN", str(value["delivery_stream_arn"])))


def deserialize_query(el: Element) -> KinesisFirehoseDestination:
    out: KinesisFirehoseDestination = {}  # type: ignore[typeddict-item]
    child_iam_role_arn = el.find("IAMRoleARN")
    if child_iam_role_arn is not None:
        out["iam_role_arn"] = str(child_iam_role_arn.text or "")
    else:
        raise DeserializationError("KinesisFirehoseDestination.iam_role_arn required")
    child_delivery_stream_arn = el.find("DeliveryStreamARN")
    if child_delivery_stream_arn is not None:
        out["delivery_stream_arn"] = str(child_delivery_stream_arn.text or "")
    else:
        raise DeserializationError(
            "KinesisFirehoseDestination.delivery_stream_arn required"
        )
    return out
