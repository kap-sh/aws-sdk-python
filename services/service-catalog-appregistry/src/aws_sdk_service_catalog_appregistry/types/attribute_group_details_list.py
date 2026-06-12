"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#AttributeGroupDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.attribute_group_details

AttributeGroupDetailsList: TypeAlias = list[
    "aws_sdk_service_catalog_appregistry.types.attribute_group_details.AttributeGroupDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeGroupDetailsList) -> list:
    import aws_sdk_service_catalog_appregistry.types.attribute_group_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog_appregistry.types.attribute_group_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AttributeGroupDetailsList:
    import aws_sdk_service_catalog_appregistry.types.attribute_group_details

    out: AttributeGroupDetailsList = []
    for item in data:
        out.append(
            aws_sdk_service_catalog_appregistry.types.attribute_group_details.deserialize_json(
                item
            )
        )
    return out
