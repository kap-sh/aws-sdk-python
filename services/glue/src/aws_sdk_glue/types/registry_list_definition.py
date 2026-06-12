"""Generated from Smithy shape ``com.amazonaws.glue#RegistryListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.registry_list_item

RegistryListDefinition: TypeAlias = list[
    "aws_sdk_glue.types.registry_list_item.RegistryListItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegistryListDefinition) -> list:
    import aws_sdk_glue.types.registry_list_item

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.registry_list_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RegistryListDefinition:
    import aws_sdk_glue.types.registry_list_item

    out: RegistryListDefinition = []
    for item in data:
        out.append(aws_sdk_glue.types.registry_list_item.deserialize_aws_json_1_1(item))
    return out
