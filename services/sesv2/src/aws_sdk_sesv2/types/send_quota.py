"""Generated from Smithy shape ``com.amazonaws.sesv2#SendQuota``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.max24_hour_send
    import aws_sdk_sesv2.types.max_send_rate
    import aws_sdk_sesv2.types.sent_last24_hours


class SendQuota(TypedDict, closed=True):
    max24_hour_send: "aws_sdk_sesv2.types.max24_hour_send.Max24HourSend"
    """<p>The maximum number of emails that you can send in the current Amazon Web Services Region over a 24-hour period. A value of -1 signifies an unlimited quota. (This value is also referred to as your <i>sending quota</i>.)</p>"""
    max_send_rate: "aws_sdk_sesv2.types.max_send_rate.MaxSendRate"
    """<p>The maximum number of emails that you can send per second in the current Amazon Web Services Region. This value is also called your <i>maximum sending rate</i> or your <i>maximum TPS (transactions per second) rate</i>.</p>"""
    sent_last24_hours: "aws_sdk_sesv2.types.sent_last24_hours.SentLast24Hours"
    """<p>The number of emails sent from your Amazon SES account in the current Amazon Web Services Region over the past 24 hours.</p>"""


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
