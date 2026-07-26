"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetObjectTypeAttributeStatisticsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.string1_to1000
    import capo_customer_profiles.types.type_name


class GetObjectTypeAttributeStatisticsRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    object_type_name: "capo_customer_profiles.types.type_name.typeName"
    """<p>The unique name of the domain object type.</p>"""
    attribute_name: "capo_customer_profiles.types.string1_to1000.string1To1000"
    """<p>The attribute name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetObjectTypeAttributeStatisticsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetObjectTypeAttributeStatisticsRequest:
    out: GetObjectTypeAttributeStatisticsRequest = {}  # type: ignore[typeddict-item]
    return out
