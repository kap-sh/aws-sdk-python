"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.entity_reference
    import aws_sdk_verifiedpermissions.types.policy_template_id
    import aws_sdk_verifiedpermissions.types.policy_type


class PolicyFilter(TypedDict):
    principal: NotRequired[
        "aws_sdk_verifiedpermissions.types.entity_reference.EntityReference"
    ]
    """<p>Filters the output to only policies that reference the specified principal.</p>"""
    resource: NotRequired[
        "aws_sdk_verifiedpermissions.types.entity_reference.EntityReference"
    ]
    """<p>Filters the output to only policies that reference the specified resource.</p>"""
    policy_type: NotRequired["aws_sdk_verifiedpermissions.types.policy_type.PolicyType"]
    """<p>Filters the output to only policies of the specified type.</p>"""
    policy_template_id: NotRequired[
        "aws_sdk_verifiedpermissions.types.policy_template_id.PolicyTemplateId"
    ]
    """<p>Filters the output to only template-linked policies that were instantiated from the specified policy template.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyFilter) -> dict:
    out: dict = {}
    if "principal" in value:
        import aws_sdk_verifiedpermissions.types.entity_reference

        out["principal"] = (
            aws_sdk_verifiedpermissions.types.entity_reference.serialize_aws_json_1_0(
                value["principal"]
            )
        )
    if "resource" in value:
        import aws_sdk_verifiedpermissions.types.entity_reference

        out["resource"] = (
            aws_sdk_verifiedpermissions.types.entity_reference.serialize_aws_json_1_0(
                value["resource"]
            )
        )
    if "policy_type" in value:
        import aws_sdk_verifiedpermissions.types.policy_type

        out["policyType"] = (
            aws_sdk_verifiedpermissions.types.policy_type.serialize_aws_json_1_0(
                value["policy_type"]
            )
        )
    if "policy_template_id" in value:
        out["policyTemplateId"] = value["policy_template_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PolicyFilter:
    out: PolicyFilter = {}  # type: ignore[typeddict-item]
    if "principal" in data:
        import aws_sdk_verifiedpermissions.types.entity_reference

        out["principal"] = (
            aws_sdk_verifiedpermissions.types.entity_reference.deserialize_aws_json_1_0(
                data["principal"]
            )
        )
    if "resource" in data:
        import aws_sdk_verifiedpermissions.types.entity_reference

        out["resource"] = (
            aws_sdk_verifiedpermissions.types.entity_reference.deserialize_aws_json_1_0(
                data["resource"]
            )
        )
    if "policyType" in data:
        import aws_sdk_verifiedpermissions.types.policy_type

        out["policy_type"] = (
            aws_sdk_verifiedpermissions.types.policy_type.deserialize_aws_json_1_0(
                data["policyType"]
            )
        )
    if "policyTemplateId" in data:
        out["policy_template_id"] = data["policyTemplateId"]
    return out
