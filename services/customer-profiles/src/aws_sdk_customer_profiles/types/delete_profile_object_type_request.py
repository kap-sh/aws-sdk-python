"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteProfileObjectTypeRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.type_name


class DeleteProfileObjectTypeRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    object_type_name: "aws_sdk_customer_profiles.types.type_name.typeName"
    """<p>The name of the profile object type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProfileObjectTypeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteProfileObjectTypeRequest:
    out: DeleteProfileObjectTypeRequest = {}  # type: ignore[typeddict-item]
    return out
