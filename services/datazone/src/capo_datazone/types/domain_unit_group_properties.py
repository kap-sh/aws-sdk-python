"""Generated from Smithy shape ``com.amazonaws.datazone#DomainUnitGroupProperties``."""

from typing_extensions import NotRequired, TypedDict


class DomainUnitGroupProperties(TypedDict, closed=True):
    group_id: NotRequired["str"]
    """<p>The ID of the domain unit group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainUnitGroupProperties) -> dict:
    out: dict = {}
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    return out


def deserialize_json(data: dict) -> DomainUnitGroupProperties:
    out: DomainUnitGroupProperties = {}  # type: ignore[typeddict-item]
    if "groupId" in data:
        out["group_id"] = data["groupId"]
    return out
