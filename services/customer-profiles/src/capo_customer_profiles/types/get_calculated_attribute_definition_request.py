"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetCalculatedAttributeDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.type_name


class GetCalculatedAttributeDefinitionRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    calculated_attribute_name: "capo_customer_profiles.types.type_name.typeName"
    """<p>The unique name of the calculated attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCalculatedAttributeDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCalculatedAttributeDefinitionRequest:
    out: GetCalculatedAttributeDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
