"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#AttributeGroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.attribute_group_id

AttributeGroupIds: TypeAlias = list[
    "aws_sdk_service_catalog_appregistry.types.attribute_group_id.AttributeGroupId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeGroupIds) -> list:
    return list(value)


def deserialize_json(data: list) -> AttributeGroupIds:
    return list(data)
