"""Generated from Smithy shape ``com.amazonaws.datazone#GetProjectInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.project_id


class GetProjectInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the project exists.</p>"""
    identifier: "capo_datazone.types.project_id.ProjectId"
    """<p>The ID of the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProjectInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProjectInput:
    out: GetProjectInput = {}  # type: ignore[typeddict-item]
    return out
