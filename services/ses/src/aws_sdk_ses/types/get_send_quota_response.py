"""Generated from Smithy shape ``com.amazonaws.ses#GetSendQuotaResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.max24_hour_send
    import aws_sdk_ses.types.max_send_rate
    import aws_sdk_ses.types.sent_last24_hours


class GetSendQuotaResponse(TypedDict):
    max24_hour_send: "aws_sdk_ses.types.max24_hour_send.Max24HourSend"
    """<p>The maximum number of emails the user is allowed to send in a 24-hour interval. A value of -1 signifies an unlimited quota.</p>"""
    max_send_rate: "aws_sdk_ses.types.max_send_rate.MaxSendRate"
    """<p>The maximum number of emails that Amazon SES can accept from the user's account per second.</p> <note> <p>The rate at which Amazon SES accepts the user's messages might be less than the maximum send rate.</p> </note>"""
    sent_last24_hours: "aws_sdk_ses.types.sent_last24_hours.SentLast24Hours"
    """<p>The number of emails sent during the previous 24 hours.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetSendQuotaResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.Max24HourSend", str(value.get("max24_hour_send", 0))))
    pairs.append((f"{prefix}.MaxSendRate", str(value.get("max_send_rate", 0))))
    pairs.append((f"{prefix}.SentLast24Hours", str(value.get("sent_last24_hours", 0))))


def deserialize_query(el: Element) -> GetSendQuotaResponse:
    out: GetSendQuotaResponse = {}  # type: ignore[typeddict-item]
    child_max24_hour_send = el.find("Max24HourSend")
    if child_max24_hour_send is not None:
        out["max24_hour_send"] = float(child_max24_hour_send.text or "")
    else:
        out["max24_hour_send"] = 0
    child_max_send_rate = el.find("MaxSendRate")
    if child_max_send_rate is not None:
        out["max_send_rate"] = float(child_max_send_rate.text or "")
    else:
        out["max_send_rate"] = 0
    child_sent_last24_hours = el.find("SentLast24Hours")
    if child_sent_last24_hours is not None:
        out["sent_last24_hours"] = float(child_sent_last24_hours.text or "")
    else:
        out["sent_last24_hours"] = 0
    return out
