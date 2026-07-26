"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyDefinitionItem``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.static_policy_definition_item
    import capo_verifiedpermissions.types.template_linked_policy_definition_item


class _PolicyDefinitionItem_static(TypedDict, closed=True):
    static: "capo_verifiedpermissions.types.static_policy_definition_item.StaticPolicyDefinitionItem"


class _PolicyDefinitionItem_templateLinked(TypedDict, closed=True):
    templateLinked: "capo_verifiedpermissions.types.template_linked_policy_definition_item.TemplateLinkedPolicyDefinitionItem"


PolicyDefinitionItem: TypeAlias = (
    _PolicyDefinitionItem_static | _PolicyDefinitionItem_templateLinked
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyDefinitionItem) -> dict:
    if "static" in value:
        import capo_verifiedpermissions.types.static_policy_definition_item

        return {
            "static": capo_verifiedpermissions.types.static_policy_definition_item.serialize_aws_json_1_0(
                value["static"]
            )
        }
    elif "templateLinked" in value:
        import capo_verifiedpermissions.types.template_linked_policy_definition_item

        return {
            "templateLinked": capo_verifiedpermissions.types.template_linked_policy_definition_item.serialize_aws_json_1_0(
                value["templateLinked"]
            )
        }
    else:
        raise SerializationError("PolicyDefinitionItem: no variant present")


def deserialize_aws_json_1_0(data: dict) -> PolicyDefinitionItem:
    if "static" in data:
        import capo_verifiedpermissions.types.static_policy_definition_item

        return {
            "static": capo_verifiedpermissions.types.static_policy_definition_item.deserialize_aws_json_1_0(
                data["static"]
            )
        }
    elif "templateLinked" in data:
        import capo_verifiedpermissions.types.template_linked_policy_definition_item

        return {
            "templateLinked": capo_verifiedpermissions.types.template_linked_policy_definition_item.deserialize_aws_json_1_0(
                data["templateLinked"]
            )
        }
    else:
        raise DeserializationError("PolicyDefinitionItem: no recognized variant key")
