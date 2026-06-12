"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetDomainLayoutRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name


class GetDomainLayoutRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    layout_definition_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the layout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainLayoutRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDomainLayoutRequest:
    out: GetDomainLayoutRequest = {}  # type: ignore[typeddict-item]
    return out
