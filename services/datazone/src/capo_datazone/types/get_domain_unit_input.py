"""Generated from Smithy shape ``com.amazonaws.datazone#GetDomainUnitInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.domain_unit_id


class GetDomainUnitInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to get a domain unit.</p>"""
    identifier: "capo_datazone.types.domain_unit_id.DomainUnitId"
    """<p>The identifier of the domain unit that you want to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainUnitInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDomainUnitInput:
    out: GetDomainUnitInput = {}  # type: ignore[typeddict-item]
    return out
