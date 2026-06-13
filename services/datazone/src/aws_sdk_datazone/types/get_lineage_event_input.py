"""Generated from Smithy shape ``com.amazonaws.datazone#GetLineageEventInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.lineage_event_identifier


class GetLineageEventInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain.</p>"""
    identifier: "aws_sdk_datazone.types.lineage_event_identifier.LineageEventIdentifier"
    """<p>The ID of the lineage event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLineageEventInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLineageEventInput:
    out: GetLineageEventInput = {}  # type: ignore[typeddict-item]
    return out
