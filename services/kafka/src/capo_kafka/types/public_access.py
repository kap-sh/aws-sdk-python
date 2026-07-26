"""Generated from Smithy shape ``com.amazonaws.kafka#PublicAccess``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string


class PublicAccess(TypedDict, closed=True):
    type: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The value DISABLED indicates that public access is turned off. SERVICE_PROVIDED_EIPS indicates that public access is turned on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublicAccess) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> PublicAccess:
    out: PublicAccess = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    return out
