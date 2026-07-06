"""Generated from Smithy shape ``com.amazonaws.datazone#OwnerPropertiesOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.owner_group_properties_output
    import aws_sdk_datazone.types.owner_user_properties_output


class _OwnerPropertiesOutput_user(TypedDict, closed=True):
    user: (
        "aws_sdk_datazone.types.owner_user_properties_output.OwnerUserPropertiesOutput"
    )


class _OwnerPropertiesOutput_group(TypedDict, closed=True):
    group: "aws_sdk_datazone.types.owner_group_properties_output.OwnerGroupPropertiesOutput"


OwnerPropertiesOutput: TypeAlias = (
    _OwnerPropertiesOutput_user | _OwnerPropertiesOutput_group
)


# --- restJson1 ser/de ---
def serialize_json(value: OwnerPropertiesOutput) -> dict:
    if "user" in value:
        import aws_sdk_datazone.types.owner_user_properties_output

        return {
            "user": aws_sdk_datazone.types.owner_user_properties_output.serialize_json(
                value["user"]
            )
        }
    elif "group" in value:
        import aws_sdk_datazone.types.owner_group_properties_output

        return {
            "group": aws_sdk_datazone.types.owner_group_properties_output.serialize_json(
                value["group"]
            )
        }
    else:
        raise SerializationError("OwnerPropertiesOutput: no variant present")


def deserialize_json(data: dict) -> OwnerPropertiesOutput:
    if "user" in data:
        import aws_sdk_datazone.types.owner_user_properties_output

        return {
            "user": aws_sdk_datazone.types.owner_user_properties_output.deserialize_json(
                data["user"]
            )
        }
    elif "group" in data:
        import aws_sdk_datazone.types.owner_group_properties_output

        return {
            "group": aws_sdk_datazone.types.owner_group_properties_output.deserialize_json(
                data["group"]
            )
        }
    else:
        raise DeserializationError("OwnerPropertiesOutput: no recognized variant key")
