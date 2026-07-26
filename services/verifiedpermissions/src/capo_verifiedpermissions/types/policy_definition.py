"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.static_policy_definition
    import capo_verifiedpermissions.types.template_linked_policy_definition


class _PolicyDefinition_static(TypedDict, closed=True):
    static: (
        "capo_verifiedpermissions.types.static_policy_definition.StaticPolicyDefinition"
    )


class _PolicyDefinition_templateLinked(TypedDict, closed=True):
    templateLinked: "capo_verifiedpermissions.types.template_linked_policy_definition.TemplateLinkedPolicyDefinition"


PolicyDefinition: TypeAlias = (
    _PolicyDefinition_static | _PolicyDefinition_templateLinked
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyDefinition) -> dict:
    if "static" in value:
        import capo_verifiedpermissions.types.static_policy_definition

        return {
            "static": capo_verifiedpermissions.types.static_policy_definition.serialize_aws_json_1_0(
                value["static"]
            )
        }
    elif "templateLinked" in value:
        import capo_verifiedpermissions.types.template_linked_policy_definition

        return {
            "templateLinked": capo_verifiedpermissions.types.template_linked_policy_definition.serialize_aws_json_1_0(
                value["templateLinked"]
            )
        }
    else:
        raise SerializationError("PolicyDefinition: no variant present")


def deserialize_aws_json_1_0(data: dict) -> PolicyDefinition:
    if "static" in data:
        import capo_verifiedpermissions.types.static_policy_definition

        return {
            "static": capo_verifiedpermissions.types.static_policy_definition.deserialize_aws_json_1_0(
                data["static"]
            )
        }
    elif "templateLinked" in data:
        import capo_verifiedpermissions.types.template_linked_policy_definition

        return {
            "templateLinked": capo_verifiedpermissions.types.template_linked_policy_definition.deserialize_aws_json_1_0(
                data["templateLinked"]
            )
        }
    else:
        raise DeserializationError("PolicyDefinition: no recognized variant key")
