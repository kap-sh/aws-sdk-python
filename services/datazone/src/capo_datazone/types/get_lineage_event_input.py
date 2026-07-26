"""Generated from Smithy shape ``com.amazonaws.datazone#GetLineageEventInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.lineage_event_identifier


class GetLineageEventInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain.</p>"""
    identifier: "capo_datazone.types.lineage_event_identifier.LineageEventIdentifier"
    """<p>The ID of the lineage event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLineageEventInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLineageEventInput:
    out: GetLineageEventInput = {}  # type: ignore[typeddict-item]
    return out
