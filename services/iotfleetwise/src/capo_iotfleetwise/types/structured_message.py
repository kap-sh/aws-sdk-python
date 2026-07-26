"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StructuredMessage``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_iotfleetwise.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.primitive_message_definition
    import capo_iotfleetwise.types.structured_message_definition
    import capo_iotfleetwise.types.structured_message_list_definition


class _StructuredMessage_primitiveMessageDefinition(TypedDict, closed=True):
    primitiveMessageDefinition: "capo_iotfleetwise.types.primitive_message_definition.PrimitiveMessageDefinition"


class _StructuredMessage_structuredMessageListDefinition(TypedDict, closed=True):
    structuredMessageListDefinition: "capo_iotfleetwise.types.structured_message_list_definition.StructuredMessageListDefinition"


class _StructuredMessage_structuredMessageDefinition(TypedDict, closed=True):
    structuredMessageDefinition: "capo_iotfleetwise.types.structured_message_definition.StructuredMessageDefinition"


StructuredMessage: TypeAlias = (
    _StructuredMessage_primitiveMessageDefinition
    | _StructuredMessage_structuredMessageListDefinition
    | _StructuredMessage_structuredMessageDefinition
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StructuredMessage) -> dict:
    if "primitiveMessageDefinition" in value:
        import capo_iotfleetwise.types.primitive_message_definition

        return {
            "primitiveMessageDefinition": capo_iotfleetwise.types.primitive_message_definition.serialize_aws_json_1_0(
                value["primitiveMessageDefinition"]
            )
        }
    elif "structuredMessageListDefinition" in value:
        import capo_iotfleetwise.types.structured_message_list_definition

        return {
            "structuredMessageListDefinition": capo_iotfleetwise.types.structured_message_list_definition.serialize_aws_json_1_0(
                value["structuredMessageListDefinition"]
            )
        }
    elif "structuredMessageDefinition" in value:
        import capo_iotfleetwise.types.structured_message_definition

        return {
            "structuredMessageDefinition": capo_iotfleetwise.types.structured_message_definition.serialize_aws_json_1_0(
                value["structuredMessageDefinition"]
            )
        }
    else:
        raise SerializationError("StructuredMessage: no variant present")


def deserialize_aws_json_1_0(data: dict) -> StructuredMessage:
    if "primitiveMessageDefinition" in data:
        import capo_iotfleetwise.types.primitive_message_definition

        return {
            "primitiveMessageDefinition": capo_iotfleetwise.types.primitive_message_definition.deserialize_aws_json_1_0(
                data["primitiveMessageDefinition"]
            )
        }
    elif "structuredMessageListDefinition" in data:
        import capo_iotfleetwise.types.structured_message_list_definition

        return {
            "structuredMessageListDefinition": capo_iotfleetwise.types.structured_message_list_definition.deserialize_aws_json_1_0(
                data["structuredMessageListDefinition"]
            )
        }
    elif "structuredMessageDefinition" in data:
        import capo_iotfleetwise.types.structured_message_definition

        return {
            "structuredMessageDefinition": capo_iotfleetwise.types.structured_message_definition.deserialize_aws_json_1_0(
                data["structuredMessageDefinition"]
            )
        }
    else:
        raise DeserializationError("StructuredMessage: no recognized variant key")
