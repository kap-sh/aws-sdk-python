"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StructuredMessage``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.primitive_message_definition
    import aws_sdk_iotfleetwise.types.structured_message_definition
    import aws_sdk_iotfleetwise.types.structured_message_list_definition


class _StructuredMessage_primitiveMessageDefinition(TypedDict):
    primitiveMessageDefinition: "aws_sdk_iotfleetwise.types.primitive_message_definition.PrimitiveMessageDefinition"


class _StructuredMessage_structuredMessageListDefinition(TypedDict):
    structuredMessageListDefinition: "aws_sdk_iotfleetwise.types.structured_message_list_definition.StructuredMessageListDefinition"


class _StructuredMessage_structuredMessageDefinition(TypedDict):
    structuredMessageDefinition: "aws_sdk_iotfleetwise.types.structured_message_definition.StructuredMessageDefinition"


StructuredMessage: TypeAlias = (
    _StructuredMessage_primitiveMessageDefinition
    | _StructuredMessage_structuredMessageListDefinition
    | _StructuredMessage_structuredMessageDefinition
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StructuredMessage) -> dict:
    if "primitiveMessageDefinition" in value:
        import aws_sdk_iotfleetwise.types.primitive_message_definition

        return {
            "primitiveMessageDefinition": aws_sdk_iotfleetwise.types.primitive_message_definition.serialize_aws_json_1_0(
                value["primitiveMessageDefinition"]
            )
        }
    elif "structuredMessageListDefinition" in value:
        import aws_sdk_iotfleetwise.types.structured_message_list_definition

        return {
            "structuredMessageListDefinition": aws_sdk_iotfleetwise.types.structured_message_list_definition.serialize_aws_json_1_0(
                value["structuredMessageListDefinition"]
            )
        }
    elif "structuredMessageDefinition" in value:
        import aws_sdk_iotfleetwise.types.structured_message_definition

        return {
            "structuredMessageDefinition": aws_sdk_iotfleetwise.types.structured_message_definition.serialize_aws_json_1_0(
                value["structuredMessageDefinition"]
            )
        }
    else:
        raise SerializationError("StructuredMessage: no variant present")


def deserialize_aws_json_1_0(data: dict) -> StructuredMessage:
    if "primitiveMessageDefinition" in data:
        import aws_sdk_iotfleetwise.types.primitive_message_definition

        return {
            "primitiveMessageDefinition": aws_sdk_iotfleetwise.types.primitive_message_definition.deserialize_aws_json_1_0(
                data["primitiveMessageDefinition"]
            )
        }
    elif "structuredMessageListDefinition" in data:
        import aws_sdk_iotfleetwise.types.structured_message_list_definition

        return {
            "structuredMessageListDefinition": aws_sdk_iotfleetwise.types.structured_message_list_definition.deserialize_aws_json_1_0(
                data["structuredMessageListDefinition"]
            )
        }
    elif "structuredMessageDefinition" in data:
        import aws_sdk_iotfleetwise.types.structured_message_definition

        return {
            "structuredMessageDefinition": aws_sdk_iotfleetwise.types.structured_message_definition.deserialize_aws_json_1_0(
                data["structuredMessageDefinition"]
            )
        }
    else:
        raise DeserializationError("StructuredMessage: no recognized variant key")
