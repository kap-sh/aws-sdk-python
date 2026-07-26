"""Generated from Smithy shape ``com.amazonaws.datazone#DomainUnitSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.domain_unit_id


class DomainUnitSummary(TypedDict, closed=True):
    name: "str"
    """<p>The name of the domain unit summary.</p>"""
    id: "capo_datazone.types.domain_unit_id.DomainUnitId"
    """<p>The ID of the domain unit summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainUnitSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> DomainUnitSummary:
    out: DomainUnitSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DomainUnitSummary.name required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DomainUnitSummary.id required")
    return out
