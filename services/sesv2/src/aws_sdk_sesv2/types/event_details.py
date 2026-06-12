"""Generated from Smithy shape ``com.amazonaws.sesv2#EventDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.bounce
    import aws_sdk_sesv2.types.complaint


class EventDetails(TypedDict):
    bounce: NotRequired["aws_sdk_sesv2.types.bounce.Bounce"]
    """<p>Information about a <code>Bounce</code> event.</p>"""
    complaint: NotRequired["aws_sdk_sesv2.types.complaint.Complaint"]
    """<p>Information about a <code>Complaint</code> event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventDetails) -> dict:
    out: dict = {}
    if "bounce" in value:
        import aws_sdk_sesv2.types.bounce

        out["Bounce"] = aws_sdk_sesv2.types.bounce.serialize_json(value["bounce"])
    if "complaint" in value:
        import aws_sdk_sesv2.types.complaint

        out["Complaint"] = aws_sdk_sesv2.types.complaint.serialize_json(
            value["complaint"]
        )
    return out


def deserialize_json(data: dict) -> EventDetails:
    out: EventDetails = {}  # type: ignore[typeddict-item]
    if "Bounce" in data:
        import aws_sdk_sesv2.types.bounce

        out["bounce"] = aws_sdk_sesv2.types.bounce.deserialize_json(data["Bounce"])
    if "Complaint" in data:
        import aws_sdk_sesv2.types.complaint

        out["complaint"] = aws_sdk_sesv2.types.complaint.deserialize_json(
            data["Complaint"]
        )
    return out
