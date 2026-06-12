"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#AttributeGroupSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.attribute_group_summary

AttributeGroupSummaries: TypeAlias = list[
    "aws_sdk_service_catalog_appregistry.types.attribute_group_summary.AttributeGroupSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeGroupSummaries) -> list:
    import aws_sdk_service_catalog_appregistry.types.attribute_group_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog_appregistry.types.attribute_group_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AttributeGroupSummaries:
    import aws_sdk_service_catalog_appregistry.types.attribute_group_summary

    out: AttributeGroupSummaries = []
    for item in data:
        out.append(
            aws_sdk_service_catalog_appregistry.types.attribute_group_summary.deserialize_json(
                item
            )
        )
    return out
