"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyDefinitionItem``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.static_policy_definition_item
    import aws_sdk_verifiedpermissions.types.template_linked_policy_definition_item


class _PolicyDefinitionItem_static(TypedDict):
    static: "aws_sdk_verifiedpermissions.types.static_policy_definition_item.StaticPolicyDefinitionItem"


class _PolicyDefinitionItem_templateLinked(TypedDict):
    templateLinked: "aws_sdk_verifiedpermissions.types.template_linked_policy_definition_item.TemplateLinkedPolicyDefinitionItem"


PolicyDefinitionItem: TypeAlias = (
    _PolicyDefinitionItem_static | _PolicyDefinitionItem_templateLinked
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyDefinitionItem) -> dict:
    if "static" in value:
        import aws_sdk_verifiedpermissions.types.static_policy_definition_item

        return {
            "static": aws_sdk_verifiedpermissions.types.static_policy_definition_item.serialize_aws_json_1_0(
                value["static"]
            )
        }
    elif "templateLinked" in value:
        import aws_sdk_verifiedpermissions.types.template_linked_policy_definition_item

        return {
            "templateLinked": aws_sdk_verifiedpermissions.types.template_linked_policy_definition_item.serialize_aws_json_1_0(
                value["templateLinked"]
            )
        }
    else:
        raise SerializationError("PolicyDefinitionItem: no variant present")


def deserialize_aws_json_1_0(data: dict) -> PolicyDefinitionItem:
    if "static" in data:
        import aws_sdk_verifiedpermissions.types.static_policy_definition_item

        return {
            "static": aws_sdk_verifiedpermissions.types.static_policy_definition_item.deserialize_aws_json_1_0(
                data["static"]
            )
        }
    elif "templateLinked" in data:
        import aws_sdk_verifiedpermissions.types.template_linked_policy_definition_item

        return {
            "templateLinked": aws_sdk_verifiedpermissions.types.template_linked_policy_definition_item.deserialize_aws_json_1_0(
                data["templateLinked"]
            )
        }
    else:
        raise DeserializationError("PolicyDefinitionItem: no recognized variant key")
