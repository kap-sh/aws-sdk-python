"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetProfileObjectTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.type_name


class GetProfileObjectTypeRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    object_type_name: "aws_sdk_customer_profiles.types.type_name.typeName"
    """<p>The name of the profile object type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProfileObjectTypeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProfileObjectTypeRequest:
    out: GetProfileObjectTypeRequest = {}  # type: ignore[typeddict-item]
    return out
