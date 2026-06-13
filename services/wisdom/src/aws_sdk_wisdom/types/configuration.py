"""Generated from Smithy shape ``com.amazonaws.wisdom#Configuration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_wisdom.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.connect_configuration


class _Configuration_connectConfiguration(TypedDict):
    connectConfiguration: (
        "aws_sdk_wisdom.types.connect_configuration.ConnectConfiguration"
    )


Configuration: TypeAlias = _Configuration_connectConfiguration


# --- restJson1 ser/de ---
def serialize_json(value: Configuration) -> dict:
    if "connectConfiguration" in value:
        import aws_sdk_wisdom.types.connect_configuration

        return {
            "connectConfiguration": aws_sdk_wisdom.types.connect_configuration.serialize_json(
                value["connectConfiguration"]
            )
        }
    else:
        raise SerializationError("Configuration: no variant present")


def deserialize_json(data: dict) -> Configuration:
    if "connectConfiguration" in data:
        import aws_sdk_wisdom.types.connect_configuration

        return {
            "connectConfiguration": aws_sdk_wisdom.types.connect_configuration.deserialize_json(
                data["connectConfiguration"]
            )
        }
    else:
        raise DeserializationError("Configuration: no recognized variant key")
