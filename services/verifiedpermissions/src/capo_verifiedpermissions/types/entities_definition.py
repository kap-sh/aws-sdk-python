"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#EntitiesDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.cedar_json
    import capo_verifiedpermissions.types.entity_list


class _EntitiesDefinition_entityList(TypedDict, closed=True):
    entityList: "capo_verifiedpermissions.types.entity_list.EntityList"


class _EntitiesDefinition_cedarJson(TypedDict, closed=True):
    cedarJson: "capo_verifiedpermissions.types.cedar_json.CedarJson"


EntitiesDefinition: TypeAlias = (
    _EntitiesDefinition_entityList | _EntitiesDefinition_cedarJson
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EntitiesDefinition) -> dict:
    if "entityList" in value:
        import capo_verifiedpermissions.types.entity_list

        return {
            "entityList": capo_verifiedpermissions.types.entity_list.serialize_aws_json_1_0(
                value["entityList"]
            )
        }
    elif "cedarJson" in value:
        return {"cedarJson": value["cedarJson"]}
    else:
        raise SerializationError("EntitiesDefinition: no variant present")


def deserialize_aws_json_1_0(data: dict) -> EntitiesDefinition:
    if "entityList" in data:
        import capo_verifiedpermissions.types.entity_list

        return {
            "entityList": capo_verifiedpermissions.types.entity_list.deserialize_aws_json_1_0(
                data["entityList"]
            )
        }
    elif "cedarJson" in data:
        return {"cedarJson": data["cedarJson"]}
    else:
        raise DeserializationError("EntitiesDefinition: no recognized variant key")
