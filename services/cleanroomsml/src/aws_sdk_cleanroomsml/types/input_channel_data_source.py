"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#InputChannelDataSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.protected_query_input_parameters


class _InputChannelDataSource_protectedQueryInputParameters(TypedDict, closed=True):
    protectedQueryInputParameters: "aws_sdk_cleanroomsml.types.protected_query_input_parameters.ProtectedQueryInputParameters"


InputChannelDataSource: TypeAlias = (
    _InputChannelDataSource_protectedQueryInputParameters
)


# --- restJson1 ser/de ---
def serialize_json(value: InputChannelDataSource) -> dict:
    if "protectedQueryInputParameters" in value:
        import aws_sdk_cleanroomsml.types.protected_query_input_parameters

        return {
            "protectedQueryInputParameters": aws_sdk_cleanroomsml.types.protected_query_input_parameters.serialize_json(
                value["protectedQueryInputParameters"]
            )
        }
    else:
        raise SerializationError("InputChannelDataSource: no variant present")


def deserialize_json(data: dict) -> InputChannelDataSource:
    if "protectedQueryInputParameters" in data:
        import aws_sdk_cleanroomsml.types.protected_query_input_parameters

        return {
            "protectedQueryInputParameters": aws_sdk_cleanroomsml.types.protected_query_input_parameters.deserialize_json(
                data["protectedQueryInputParameters"]
            )
        }
    else:
        raise DeserializationError("InputChannelDataSource: no recognized variant key")
