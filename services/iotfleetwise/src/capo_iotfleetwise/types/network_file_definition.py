"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#NetworkFileDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_iotfleetwise.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.can_dbc_definition


class _NetworkFileDefinition_canDbc(TypedDict, closed=True):
    canDbc: "capo_iotfleetwise.types.can_dbc_definition.CanDbcDefinition"


NetworkFileDefinition: TypeAlias = _NetworkFileDefinition_canDbc


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NetworkFileDefinition) -> dict:
    if "canDbc" in value:
        import capo_iotfleetwise.types.can_dbc_definition

        return {
            "canDbc": capo_iotfleetwise.types.can_dbc_definition.serialize_aws_json_1_0(
                value["canDbc"]
            )
        }
    else:
        raise SerializationError("NetworkFileDefinition: no variant present")


def deserialize_aws_json_1_0(data: dict) -> NetworkFileDefinition:
    if "canDbc" in data:
        import capo_iotfleetwise.types.can_dbc_definition

        return {
            "canDbc": capo_iotfleetwise.types.can_dbc_definition.deserialize_aws_json_1_0(
                data["canDbc"]
            )
        }
    else:
        raise DeserializationError("NetworkFileDefinition: no recognized variant key")
