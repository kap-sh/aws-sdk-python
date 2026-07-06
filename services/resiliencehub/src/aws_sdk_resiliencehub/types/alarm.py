"""Generated from Smithy shape ``com.amazonaws.resiliencehub#Alarm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.string255


class Alarm(TypedDict, closed=True):
    alarm_arn: NotRequired["aws_sdk_resiliencehub.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of the Amazon CloudWatch alarm.</p>"""
    source: NotRequired["aws_sdk_resiliencehub.types.string255.String255"]
    """<p>Indicates the source of the Amazon CloudWatch alarm. That is, it indicates if the alarm was created using Resilience Hub recommendation (<code>AwsResilienceHub</code>), or if you had created the alarm in Amazon CloudWatch (<code>Customer</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Alarm) -> dict:
    out: dict = {}
    if "alarm_arn" in value:
        out["alarmArn"] = value["alarm_arn"]
    if "source" in value:
        out["source"] = value["source"]
    return out


def deserialize_json(data: dict) -> Alarm:
    out: Alarm = {}  # type: ignore[typeddict-item]
    if "alarmArn" in data:
        out["alarm_arn"] = data["alarmArn"]
    if "source" in data:
        out["source"] = data["source"]
    return out
