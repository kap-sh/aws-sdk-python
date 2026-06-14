"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#EntityReference``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.entity_identifier


class _EntityReference_unspecified(TypedDict):
    unspecified: "bool"


class _EntityReference_identifier(TypedDict):
    identifier: "aws_sdk_verifiedpermissions.types.entity_identifier.EntityIdentifier"


EntityReference: TypeAlias = _EntityReference_unspecified | _EntityReference_identifier


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EntityReference) -> dict:
    if "unspecified" in value:
        return {"unspecified": value["unspecified"]}
    elif "identifier" in value:
        import aws_sdk_verifiedpermissions.types.entity_identifier

        return {
            "identifier": aws_sdk_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
                value["identifier"]
            )
        }
    else:
        raise SerializationError("EntityReference: no variant present")


def deserialize_aws_json_1_0(data: dict) -> EntityReference:
    if "unspecified" in data:
        return {"unspecified": data["unspecified"]}
    elif "identifier" in data:
        import aws_sdk_verifiedpermissions.types.entity_identifier

        return {
            "identifier": aws_sdk_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                data["identifier"]
            )
        }
    else:
        raise DeserializationError("EntityReference: no recognized variant key")
