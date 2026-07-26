"""Generated from Smithy shape ``com.amazonaws.datazone#PostLineageEventOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.lineage_event_identifier


class PostLineageEventOutput(TypedDict, closed=True):
    id: NotRequired[
        "capo_datazone.types.lineage_event_identifier.LineageEventIdentifier"
    ]
    """<p>The ID of the lineage event.</p>"""
    domain_id: NotRequired["capo_datazone.types.domain_id.DomainId"]
    """<p>The ID of the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostLineageEventOutput) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    return out


def deserialize_json(data: dict) -> PostLineageEventOutput:
    out: PostLineageEventOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    return out
