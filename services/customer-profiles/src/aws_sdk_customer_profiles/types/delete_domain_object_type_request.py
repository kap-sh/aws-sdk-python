"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteDomainObjectTypeRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.type_name


class DeleteDomainObjectTypeRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    object_type_name: "aws_sdk_customer_profiles.types.type_name.typeName"
    """<p>The unique name of the domain object type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainObjectTypeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDomainObjectTypeRequest:
    out: DeleteDomainObjectTypeRequest = {}  # type: ignore[typeddict-item]
    return out
