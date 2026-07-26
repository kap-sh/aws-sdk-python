"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationResourcePropertyFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.integration_resource_property_filter

IntegrationResourcePropertyFilterList: TypeAlias = list[
    "capo_glue.types.integration_resource_property_filter.IntegrationResourcePropertyFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationResourcePropertyFilterList) -> list:
    import capo_glue.types.integration_resource_property_filter

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.integration_resource_property_filter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IntegrationResourcePropertyFilterList:
    import capo_glue.types.integration_resource_property_filter

    out: IntegrationResourcePropertyFilterList = []
    for item in data:
        out.append(
            capo_glue.types.integration_resource_property_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
