"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetDomainLayoutRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name


class GetDomainLayoutRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    layout_definition_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the layout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainLayoutRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDomainLayoutRequest:
    out: GetDomainLayoutRequest = {}  # type: ignore[typeddict-item]
    return out
