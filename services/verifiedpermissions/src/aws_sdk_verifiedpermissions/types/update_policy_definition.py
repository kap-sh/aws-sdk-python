"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#UpdatePolicyDefinition``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.update_static_policy_definition


class _UpdatePolicyDefinition_static(TypedDict):
    static: "aws_sdk_verifiedpermissions.types.update_static_policy_definition.UpdateStaticPolicyDefinition"


UpdatePolicyDefinition: TypeAlias = _UpdatePolicyDefinition_static


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdatePolicyDefinition) -> dict:
    if "static" in value:
        import aws_sdk_verifiedpermissions.types.update_static_policy_definition

        return {
            "static": aws_sdk_verifiedpermissions.types.update_static_policy_definition.serialize_aws_json_1_0(
                value["static"]
            )
        }
    else:
        raise SerializationError("UpdatePolicyDefinition: no variant present")


def deserialize_aws_json_1_0(data: dict) -> UpdatePolicyDefinition:
    if "static" in data:
        import aws_sdk_verifiedpermissions.types.update_static_policy_definition

        return {
            "static": aws_sdk_verifiedpermissions.types.update_static_policy_definition.deserialize_aws_json_1_0(
                data["static"]
            )
        }
    else:
        raise DeserializationError("UpdatePolicyDefinition: no recognized variant key")
