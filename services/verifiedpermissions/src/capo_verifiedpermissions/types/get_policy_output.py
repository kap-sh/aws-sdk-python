"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#GetPolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.action_identifier_list
    import capo_verifiedpermissions.types.entity_identifier
    import capo_verifiedpermissions.types.policy_definition_detail
    import capo_verifiedpermissions.types.policy_effect
    import capo_verifiedpermissions.types.policy_id
    import capo_verifiedpermissions.types.policy_name
    import capo_verifiedpermissions.types.policy_store_id
    import capo_verifiedpermissions.types.policy_type
    import capo_verifiedpermissions.types.timestamp_format


class GetPolicyOutput(TypedDict, closed=True):
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The ID of the policy store that contains the policy that you want information about.</p>"""
    policy_id: "capo_verifiedpermissions.types.policy_id.PolicyId"
    """<p>The unique ID of the policy that you want information about.</p>"""
    policy_type: "capo_verifiedpermissions.types.policy_type.PolicyType"
    """<p>The type of the policy.</p>"""
    principal: NotRequired[
        "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
    ]
    """<p>The principal specified in the policy's scope. This element isn't included in the response when <code>Principal</code> isn't present in the policy content.</p>"""
    resource: NotRequired[
        "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
    ]
    """<p>The resource specified in the policy's scope. This element isn't included in the response when <code>Resource</code> isn't present in the policy content.</p>"""
    actions: NotRequired[
        "capo_verifiedpermissions.types.action_identifier_list.ActionIdentifierList"
    ]
    r"""<p>The action that a policy permits or forbids. For example, <code>{\"actions\": [{\"actionId\": \"ViewPhoto\", \"actionType\": \"PhotoFlash::Action\"}, {\"entityID\": \"SharePhoto\", \"entityType\": \"PhotoFlash::Action\"}]}</code>.</p>"""
    definition: (
        "capo_verifiedpermissions.types.policy_definition_detail.PolicyDefinitionDetail"
    )
    """<p>The definition of the requested policy.</p>"""
    created_date: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time that the policy was originally created.</p>"""
    last_updated_date: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time that the policy was last updated.</p>"""
    effect: NotRequired["capo_verifiedpermissions.types.policy_effect.PolicyEffect"]
    r"""<p>The effect of the decision that a policy returns to an authorization request. For example, <code>\"effect\": \"Permit\"</code>.</p>"""
    name: NotRequired["capo_verifiedpermissions.types.policy_name.PolicyName"]
    """<p>The name of the policy, if one was assigned when the policy was created or last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetPolicyOutput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    out["policyId"] = value["policy_id"]
    import capo_verifiedpermissions.types.policy_type

    out["policyType"] = (
        capo_verifiedpermissions.types.policy_type.serialize_aws_json_1_0(
            value["policy_type"]
        )
    )
    if "principal" in value:
        import capo_verifiedpermissions.types.entity_identifier

        out["principal"] = (
            capo_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
                value["principal"]
            )
        )
    if "resource" in value:
        import capo_verifiedpermissions.types.entity_identifier

        out["resource"] = (
            capo_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
                value["resource"]
            )
        )
    if "actions" in value:
        import capo_verifiedpermissions.types.action_identifier_list

        out["actions"] = (
            capo_verifiedpermissions.types.action_identifier_list.serialize_aws_json_1_0(
                value["actions"]
            )
        )
    import capo_verifiedpermissions.types.policy_definition_detail

    out["definition"] = (
        capo_verifiedpermissions.types.policy_definition_detail.serialize_aws_json_1_0(
            value["definition"]
        )
    )
    import capo_verifiedpermissions.types.timestamp_format

    out["createdDate"] = (
        capo_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
            value["created_date"]
        )
    )
    import capo_verifiedpermissions.types.timestamp_format

    out["lastUpdatedDate"] = (
        capo_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
            value["last_updated_date"]
        )
    )
    if "effect" in value:
        import capo_verifiedpermissions.types.policy_effect

        out["effect"] = (
            capo_verifiedpermissions.types.policy_effect.serialize_aws_json_1_0(
                value["effect"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetPolicyOutput:
    out: GetPolicyOutput = {}  # type: ignore[typeddict-item]
    if "policyStoreId" in data:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("GetPolicyOutput.policy_store_id required")
    if "policyId" in data:
        out["policy_id"] = data["policyId"]
    else:
        raise DeserializationError("GetPolicyOutput.policy_id required")
    if "policyType" in data:
        import capo_verifiedpermissions.types.policy_type

        out["policy_type"] = (
            capo_verifiedpermissions.types.policy_type.deserialize_aws_json_1_0(
                data["policyType"]
            )
        )
    else:
        raise DeserializationError("GetPolicyOutput.policy_type required")
    if "principal" in data:
        import capo_verifiedpermissions.types.entity_identifier

        out["principal"] = (
            capo_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                data["principal"]
            )
        )
    if "resource" in data:
        import capo_verifiedpermissions.types.entity_identifier

        out["resource"] = (
            capo_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                data["resource"]
            )
        )
    if "actions" in data:
        import capo_verifiedpermissions.types.action_identifier_list

        out["actions"] = (
            capo_verifiedpermissions.types.action_identifier_list.deserialize_aws_json_1_0(
                data["actions"]
            )
        )
    if "definition" in data:
        import capo_verifiedpermissions.types.policy_definition_detail

        out["definition"] = (
            capo_verifiedpermissions.types.policy_definition_detail.deserialize_aws_json_1_0(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("GetPolicyOutput.definition required")
    if "createdDate" in data:
        import capo_verifiedpermissions.types.timestamp_format

        out["created_date"] = (
            capo_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["createdDate"]
            )
        )
    else:
        raise DeserializationError("GetPolicyOutput.created_date required")
    if "lastUpdatedDate" in data:
        import capo_verifiedpermissions.types.timestamp_format

        out["last_updated_date"] = (
            capo_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["lastUpdatedDate"]
            )
        )
    else:
        raise DeserializationError("GetPolicyOutput.last_updated_date required")
    if "effect" in data:
        import capo_verifiedpermissions.types.policy_effect

        out["effect"] = (
            capo_verifiedpermissions.types.policy_effect.deserialize_aws_json_1_0(
                data["effect"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    return out
