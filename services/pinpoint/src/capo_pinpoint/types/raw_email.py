"""Generated from Smithy shape ``com.amazonaws.pinpoint#RawEmail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__blob


class RawEmail(TypedDict, closed=True):
    data: NotRequired["capo_pinpoint.types.__blob.__blob"]
    """<p>The email message, represented as a raw MIME message. The entire message must be base64 encoded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RawEmail) -> dict:
    out: dict = {}
    if "data" in value:
        import capo_pinpoint.types.__blob

        out["Data"] = capo_pinpoint.types.__blob.serialize_json(value["data"])
    return out


def deserialize_json(data: dict) -> RawEmail:
    out: RawEmail = {}  # type: ignore[typeddict-item]
    if "Data" in data:
        import capo_pinpoint.types.__blob

        out["data"] = capo_pinpoint.types.__blob.deserialize_json(data["Data"])
    return out
