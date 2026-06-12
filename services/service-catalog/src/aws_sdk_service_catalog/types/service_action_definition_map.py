"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ServiceActionDefinitionMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.service_action_definition_key
    import aws_sdk_service_catalog.types.service_action_definition_value

ServiceActionDefinitionMap: TypeAlias = dict[
    "aws_sdk_service_catalog.types.service_action_definition_key.ServiceActionDefinitionKey",
    "aws_sdk_service_catalog.types.service_action_definition_value.ServiceActionDefinitionValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ServiceActionDefinitionMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_service_catalog.types.service_action_definition_key

        out[
            aws_sdk_service_catalog.types.service_action_definition_key.serialize_aws_json_1_1(
                key
            )
        ] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceActionDefinitionMap:
    out: ServiceActionDefinitionMap = {}
    for key, value in data.items():
        import aws_sdk_service_catalog.types.service_action_definition_key

        out[
            aws_sdk_service_catalog.types.service_action_definition_key.deserialize_aws_json_1_1(
                key
            )
        ] = value
    return out
