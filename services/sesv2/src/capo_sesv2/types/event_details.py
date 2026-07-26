"""Generated from Smithy shape ``com.amazonaws.sesv2#EventDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.bounce
    import capo_sesv2.types.complaint


class EventDetails(TypedDict, closed=True):
    bounce: NotRequired["capo_sesv2.types.bounce.Bounce"]
    """<p>Information about a <code>Bounce</code> event.</p>"""
    complaint: NotRequired["capo_sesv2.types.complaint.Complaint"]
    """<p>Information about a <code>Complaint</code> event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventDetails) -> dict:
    out: dict = {}
    if "bounce" in value:
        import capo_sesv2.types.bounce

        out["Bounce"] = capo_sesv2.types.bounce.serialize_json(value["bounce"])
    if "complaint" in value:
        import capo_sesv2.types.complaint

        out["Complaint"] = capo_sesv2.types.complaint.serialize_json(value["complaint"])
    return out


def deserialize_json(data: dict) -> EventDetails:
    out: EventDetails = {}  # type: ignore[typeddict-item]
    if "Bounce" in data:
        import capo_sesv2.types.bounce

        out["bounce"] = capo_sesv2.types.bounce.deserialize_json(data["Bounce"])
    if "Complaint" in data:
        import capo_sesv2.types.complaint

        out["complaint"] = capo_sesv2.types.complaint.deserialize_json(
            data["Complaint"]
        )
    return out
