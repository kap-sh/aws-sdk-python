"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileAttributeValuesRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.string1_to255


class ProfileAttributeValuesRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique identifier of the domain.</p>"""
    attribute_name: "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    """<p>The attribute name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileAttributeValuesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ProfileAttributeValuesRequest:
    out: ProfileAttributeValuesRequest = {}  # type: ignore[typeddict-item]
    return out
