"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#KinesisFirehoseDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.delivery_stream_arn
    import capo_pinpoint_sms_voice_v2.types.iam_role_arn


class KinesisFirehoseDestination(TypedDict, closed=True):
    iam_role_arn: "capo_pinpoint_sms_voice_v2.types.iam_role_arn.IamRoleArn"
    """<p>The ARN of an Identity and Access Management role that is able to write event data to an Amazon Data Firehose destination.</p>"""
    delivery_stream_arn: (
        "capo_pinpoint_sms_voice_v2.types.delivery_stream_arn.DeliveryStreamArn"
    )
    """<p>The Amazon Resource Name (ARN) of the delivery stream.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KinesisFirehoseDestination) -> dict:
    out: dict = {}
    out["IamRoleArn"] = value["iam_role_arn"]
    out["DeliveryStreamArn"] = value["delivery_stream_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> KinesisFirehoseDestination:
    out: KinesisFirehoseDestination = {}  # type: ignore[typeddict-item]
    if "IamRoleArn" in data:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        raise DeserializationError("KinesisFirehoseDestination.iam_role_arn required")
    if "DeliveryStreamArn" in data:
        out["delivery_stream_arn"] = data["DeliveryStreamArn"]
    else:
        raise DeserializationError(
            "KinesisFirehoseDestination.delivery_stream_arn required"
        )
    return out
