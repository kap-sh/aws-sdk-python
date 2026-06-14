"""Generated from Smithy shape ``com.amazonaws.datazone#DomainUnitUserProperties``."""

from typing import TypedDict

from typing_extensions import NotRequired


class DomainUnitUserProperties(TypedDict):
    user_id: NotRequired["str"]
    """<p>The ID of teh domain unit user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainUnitUserProperties) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["userId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> DomainUnitUserProperties:
    out: DomainUnitUserProperties = {}  # type: ignore[typeddict-item]
    if "userId" in data:
        out["user_id"] = data["userId"]
    return out
