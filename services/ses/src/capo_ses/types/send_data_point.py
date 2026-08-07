"""Generated from Smithy shape ``com.amazonaws.ses#SendDataPoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.counter
    import capo_ses.types.timestamp


class SendDataPoint(TypedDict, closed=True):
    timestamp: NotRequired["capo_ses.types.timestamp.Timestamp"]
    """<p>Time of the data point.</p>"""
    delivery_attempts: "capo_ses.types.counter.Counter"
    """<p>Number of emails that have been sent.</p>"""
    bounces: "capo_ses.types.counter.Counter"
    """<p>Number of emails that have bounced.</p>"""
    complaints: "capo_ses.types.counter.Counter"
    """<p>Number of unwanted emails that were rejected by recipients.</p>"""
    rejects: "capo_ses.types.counter.Counter"
    """<p>Number of emails rejected by Amazon SES.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SendDataPoint, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "timestamp" in value:
        import capo_ses.types.timestamp

        capo_ses.types.timestamp.serialize_query(
            value["timestamp"], pairs, f"{key_prefix}Timestamp"
        )
    pairs.append(
        (f"{key_prefix}DeliveryAttempts", str(value.get("delivery_attempts", 0)))
    )
    pairs.append((f"{key_prefix}Bounces", str(value.get("bounces", 0))))
    pairs.append((f"{key_prefix}Complaints", str(value.get("complaints", 0))))
    pairs.append((f"{key_prefix}Rejects", str(value.get("rejects", 0))))


def deserialize_query(el: Element) -> SendDataPoint:
    out: SendDataPoint = {}  # type: ignore[typeddict-item]
    child_timestamp = el.find("Timestamp")
    if child_timestamp is not None:
        import capo_ses.types.timestamp

        out["timestamp"] = capo_ses.types.timestamp.deserialize_query(child_timestamp)
    child_delivery_attempts = el.find("DeliveryAttempts")
    if child_delivery_attempts is not None:
        out["delivery_attempts"] = int(child_delivery_attempts.text or "")
    else:
        out["delivery_attempts"] = 0
    child_bounces = el.find("Bounces")
    if child_bounces is not None:
        out["bounces"] = int(child_bounces.text or "")
    else:
        out["bounces"] = 0
    child_complaints = el.find("Complaints")
    if child_complaints is not None:
        out["complaints"] = int(child_complaints.text or "")
    else:
        out["complaints"] = 0
    child_rejects = el.find("Rejects")
    if child_rejects is not None:
        out["rejects"] = int(child_rejects.text or "")
    else:
        out["rejects"] = 0
    return out
