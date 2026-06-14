"""Generated from Smithy shape ``com.amazonaws.datazone#OwnerProperties``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.owner_group_properties
    import aws_sdk_datazone.types.owner_user_properties


class _OwnerProperties_user(TypedDict):
    user: "aws_sdk_datazone.types.owner_user_properties.OwnerUserProperties"


class _OwnerProperties_group(TypedDict):
    group: "aws_sdk_datazone.types.owner_group_properties.OwnerGroupProperties"


OwnerProperties: TypeAlias = _OwnerProperties_user | _OwnerProperties_group


# --- restJson1 ser/de ---
def serialize_json(value: OwnerProperties) -> dict:
    if "user" in value:
        import aws_sdk_datazone.types.owner_user_properties

        return {
            "user": aws_sdk_datazone.types.owner_user_properties.serialize_json(
                value["user"]
            )
        }
    elif "group" in value:
        import aws_sdk_datazone.types.owner_group_properties

        return {
            "group": aws_sdk_datazone.types.owner_group_properties.serialize_json(
                value["group"]
            )
        }
    else:
        raise SerializationError("OwnerProperties: no variant present")


def deserialize_json(data: dict) -> OwnerProperties:
    if "user" in data:
        import aws_sdk_datazone.types.owner_user_properties

        return {
            "user": aws_sdk_datazone.types.owner_user_properties.deserialize_json(
                data["user"]
            )
        }
    elif "group" in data:
        import aws_sdk_datazone.types.owner_group_properties

        return {
            "group": aws_sdk_datazone.types.owner_group_properties.deserialize_json(
                data["group"]
            )
        }
    else:
        raise DeserializationError("OwnerProperties: no recognized variant key")
