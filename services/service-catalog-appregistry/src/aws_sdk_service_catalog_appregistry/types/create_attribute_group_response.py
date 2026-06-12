"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#CreateAttributeGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.attribute_group


class CreateAttributeGroupResponse(TypedDict):
    attribute_group: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.attribute_group.AttributeGroup"
    ]
    """<p>Information about the attribute group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAttributeGroupResponse) -> dict:
    out: dict = {}
    if "attribute_group" in value:
        import aws_sdk_service_catalog_appregistry.types.attribute_group

        out["attributeGroup"] = (
            aws_sdk_service_catalog_appregistry.types.attribute_group.serialize_json(
                value["attribute_group"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateAttributeGroupResponse:
    out: CreateAttributeGroupResponse = {}  # type: ignore[typeddict-item]
    if "attributeGroup" in data:
        import aws_sdk_service_catalog_appregistry.types.attribute_group

        out["attribute_group"] = (
            aws_sdk_service_catalog_appregistry.types.attribute_group.deserialize_json(
                data["attributeGroup"]
            )
        )
    return out
