"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ContextDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.cedar_json
    import aws_sdk_verifiedpermissions.types.context_map


class _ContextDefinition_contextMap(TypedDict, closed=True):
    contextMap: "aws_sdk_verifiedpermissions.types.context_map.ContextMap"


class _ContextDefinition_cedarJson(TypedDict, closed=True):
    cedarJson: "aws_sdk_verifiedpermissions.types.cedar_json.CedarJson"


ContextDefinition: TypeAlias = (
    _ContextDefinition_contextMap | _ContextDefinition_cedarJson
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContextDefinition) -> dict:
    if "contextMap" in value:
        import aws_sdk_verifiedpermissions.types.context_map

        return {
            "contextMap": aws_sdk_verifiedpermissions.types.context_map.serialize_aws_json_1_0(
                value["contextMap"]
            )
        }
    elif "cedarJson" in value:
        return {"cedarJson": value["cedarJson"]}
    else:
        raise SerializationError("ContextDefinition: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ContextDefinition:
    if "contextMap" in data:
        import aws_sdk_verifiedpermissions.types.context_map

        return {
            "contextMap": aws_sdk_verifiedpermissions.types.context_map.deserialize_aws_json_1_0(
                data["contextMap"]
            )
        }
    elif "cedarJson" in data:
        return {"cedarJson": data["cedarJson"]}
    else:
        raise DeserializationError("ContextDefinition: no recognized variant key")
