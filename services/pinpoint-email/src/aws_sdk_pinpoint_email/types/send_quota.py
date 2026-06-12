"""Generated from Smithy shape ``com.amazonaws.pinpointemail#SendQuota``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.max24_hour_send
    import aws_sdk_pinpoint_email.types.max_send_rate
    import aws_sdk_pinpoint_email.types.sent_last24_hours


class SendQuota(TypedDict):
    max24_hour_send: "aws_sdk_pinpoint_email.types.max24_hour_send.Max24HourSend"
    """<p>The maximum number of emails that you can send in the current AWS Region over a 24-hour period. This value is also called your <i>sending quota</i>.</p>"""
    max_send_rate: "aws_sdk_pinpoint_email.types.max_send_rate.MaxSendRate"
    """<p>The maximum number of emails that you can send per second in the current AWS Region. This value is also called your <i>maximum sending rate</i> or your <i>maximum TPS (transactions per second) rate</i>.</p>"""
    sent_last24_hours: "aws_sdk_pinpoint_email.types.sent_last24_hours.SentLast24Hours"
    """<p>The number of emails sent from your Amazon Pinpoint account in the current AWS Region over the past 24 hours.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendQuota) -> dict:
    out: dict = {}
    out["Max24HourSend"] = value.get("max24_hour_send", 0)
    out["MaxSendRate"] = value.get("max_send_rate", 0)
    out["SentLast24Hours"] = value.get("sent_last24_hours", 0)
    return out


def deserialize_json(data: dict) -> SendQuota:
    out: SendQuota = {}  # type: ignore[typeddict-item]
    if "Max24HourSend" in data:
        out["max24_hour_send"] = data["Max24HourSend"]
    else:
        out["max24_hour_send"] = 0
    if "MaxSendRate" in data:
        out["max_send_rate"] = data["MaxSendRate"]
    else:
        out["max_send_rate"] = 0
    if "SentLast24Hours" in data:
        out["sent_last24_hours"] = data["SentLast24Hours"]
    else:
        out["sent_last24_hours"] = 0
    return out
