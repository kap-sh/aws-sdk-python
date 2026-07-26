"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#DeleteAttributeGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.attribute_group_specifier


class DeleteAttributeGroupRequest(TypedDict, closed=True):
    attribute_group: "capo_service_catalog_appregistry.types.attribute_group_specifier.AttributeGroupSpecifier"
    """<p> The name, ID, or ARN of the attribute group that holds the attributes to describe the application. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAttributeGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAttributeGroupRequest:
    out: DeleteAttributeGroupRequest = {}  # type: ignore[typeddict-item]
    return out
