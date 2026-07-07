"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetCalculatedAttributeForProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.type_name
    import aws_sdk_customer_profiles.types.uuid


class GetCalculatedAttributeForProfileRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    profile_id: "aws_sdk_customer_profiles.types.uuid.uuid"
    """<p>The unique identifier of a customer profile.</p>"""
    calculated_attribute_name: "aws_sdk_customer_profiles.types.type_name.typeName"
    """<p>The unique name of the calculated attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCalculatedAttributeForProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCalculatedAttributeForProfileRequest:
    out: GetCalculatedAttributeForProfileRequest = {}  # type: ignore[typeddict-item]
    return out
