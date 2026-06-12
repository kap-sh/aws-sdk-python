"""Generated from Smithy shape ``com.amazonaws.sesv2#StatusRecord``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.sending_status
    import aws_sdk_sesv2.types.status_cause
    import aws_sdk_sesv2.types.timestamp


class StatusRecord(TypedDict):
    status: NotRequired["aws_sdk_sesv2.types.sending_status.SendingStatus"]
    """<p>The current sending status. This can be one of the following:</p> <ul> <li> <p> <code>ENABLED</code> – Sending is allowed.</p> </li> <li> <p> <code>DISABLED</code> – Sending is prevented.</p> </li> <li> <p> <code>REINSTATED</code> – Sending is allowed even with active reputation findings.</p> </li> </ul>"""
    cause: NotRequired["aws_sdk_sesv2.types.status_cause.StatusCause"]
    """<p>A description of the reason for the current status, or null if no specific cause is available.</p>"""
    last_updated_timestamp: NotRequired["aws_sdk_sesv2.types.timestamp.Timestamp"]
    """<p>The timestamp when this status was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatusRecord) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_sesv2.types.sending_status

        out["Status"] = aws_sdk_sesv2.types.sending_status.serialize_json(
            value["status"]
        )
    if "cause" in value:
        out["Cause"] = value["cause"]
    if "last_updated_timestamp" in value:
        import aws_sdk_sesv2.types.timestamp

        out["LastUpdatedTimestamp"] = aws_sdk_sesv2.types.timestamp.serialize_json(
            value["last_updated_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> StatusRecord:
    out: StatusRecord = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_sesv2.types.sending_status

        out["status"] = aws_sdk_sesv2.types.sending_status.deserialize_json(
            data["Status"]
        )
    if "Cause" in data:
        out["cause"] = data["Cause"]
    if "LastUpdatedTimestamp" in data:
        import aws_sdk_sesv2.types.timestamp

        out["last_updated_timestamp"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["LastUpdatedTimestamp"]
        )
    return out
