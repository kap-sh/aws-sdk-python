"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#EntityReference``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.entity_identifier


class _EntityReference_unspecified(TypedDict, closed=True):
    unspecified: "bool"


class _EntityReference_identifier(TypedDict, closed=True):
    identifier: "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"


EntityReference: TypeAlias = _EntityReference_unspecified | _EntityReference_identifier


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EntityReference) -> dict:
    if "unspecified" in value:
        return {"unspecified": value["unspecified"]}
    elif "identifier" in value:
        import capo_verifiedpermissions.types.entity_identifier

        return {
            "identifier": capo_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
                value["identifier"]
            )
        }
    else:
        raise SerializationError("EntityReference: no variant present")


def deserialize_aws_json_1_0(data: dict) -> EntityReference:
    if "unspecified" in data:
        return {"unspecified": data["unspecified"]}
    elif "identifier" in data:
        import capo_verifiedpermissions.types.entity_identifier

        return {
            "identifier": capo_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                data["identifier"]
            )
        }
    else:
        raise DeserializationError("EntityReference: no recognized variant key")
