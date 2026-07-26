"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationResourcePropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.integration_resource_property

IntegrationResourcePropertyList: TypeAlias = list[
    "capo_glue.types.integration_resource_property.IntegrationResourceProperty"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationResourcePropertyList) -> list:
    import capo_glue.types.integration_resource_property

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.integration_resource_property.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IntegrationResourcePropertyList:
    import capo_glue.types.integration_resource_property

    out: IntegrationResourcePropertyList = []
    for item in data:
        out.append(
            capo_glue.types.integration_resource_property.deserialize_aws_json_1_1(item)
        )
    return out
