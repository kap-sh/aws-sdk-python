"""Generated from Smithy shape ``com.amazonaws.connectcases#Section``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_connectcases.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_group


class _Section_fieldGroup(TypedDict):
    fieldGroup: "aws_sdk_connectcases.types.field_group.FieldGroup"


Section: TypeAlias = _Section_fieldGroup


# --- restJson1 ser/de ---
def serialize_json(value: Section) -> dict:
    if "fieldGroup" in value:
        import aws_sdk_connectcases.types.field_group

        return {
            "fieldGroup": aws_sdk_connectcases.types.field_group.serialize_json(
                value["fieldGroup"]
            )
        }
    else:
        raise SerializationError("Section: no variant present")


def deserialize_json(data: dict) -> Section:
    if "fieldGroup" in data:
        import aws_sdk_connectcases.types.field_group

        return {
            "fieldGroup": aws_sdk_connectcases.types.field_group.deserialize_json(
                data["fieldGroup"]
            )
        }
    else:
        raise DeserializationError("Section: no recognized variant key")
