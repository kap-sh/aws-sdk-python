"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#UpdatePolicyInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.policy_id
    import aws_sdk_verifiedpermissions.types.policy_name
    import aws_sdk_verifiedpermissions.types.policy_store_id
    import aws_sdk_verifiedpermissions.types.update_policy_definition


class UpdatePolicyInput(TypedDict):
    policy_store_id: "aws_sdk_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    r"""<p>Specifies the ID of the policy store that contains the policy that you want to update.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html\">ListPolicyStoreAliases</a>.</p>"""
    policy_id: "aws_sdk_verifiedpermissions.types.policy_id.PolicyId"
    r"""<p>Specifies the ID of the policy that you want to update. To find this value, you can use <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicies.html\">ListPolicies</a>.</p> <p>You can use the policy name in place of the policy ID. When using a name, prefix it with <code>name/</code>. For example:</p> <ul> <li> <p>ID: <code>SPEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Name: <code>name/example-policy</code> </p> </li> </ul>"""
    definition: NotRequired[
        "aws_sdk_verifiedpermissions.types.update_policy_definition.UpdatePolicyDefinition"
    ]
    """<p>Specifies the updated policy content that you want to replace on the specified policy. The content must be valid Cedar policy language text.</p> <p>If you don't specify this parameter, the existing policy definition remains unchanged.</p> <p>You can change only the following elements from the policy definition:</p> <ul> <li> <p>The <code>action</code> referenced by the policy.</p> </li> <li> <p>Any conditional clauses, such as <code>when</code> or <code>unless</code> clauses.</p> </li> </ul> <p>You <b>can't</b> change the following elements:</p> <ul> <li> <p>Changing from <code>static</code> to <code>templateLinked</code>.</p> </li> <li> <p>Changing the effect of the policy from <code>permit</code> or <code>forbid</code>.</p> </li> <li> <p>The <code>principal</code> referenced by the policy.</p> </li> <li> <p>The <code>resource</code> referenced by the policy.</p> </li> </ul>"""
    name: NotRequired["aws_sdk_verifiedpermissions.types.policy_name.PolicyName"]
    r"""<p>Specifies a name for the policy that is unique among all policies within the policy store. You can use the name in place of the policy ID in API operations that reference the policy. The name must be prefixed with <code>name/</code>.</p> <note> <p>If you don't include the name in an update request, the existing name is unchanged. To remove a name, set it to an empty string (<code>\"\"</code>).</p> </note> <p>If you specify a name that is already associated with another policy in the policy store, you receive a <code>ConflictException</code> error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdatePolicyInput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    out["policyId"] = value["policy_id"]
    if "definition" in value:
        import aws_sdk_verifiedpermissions.types.update_policy_definition

        out["definition"] = (
            aws_sdk_verifiedpermissions.types.update_policy_definition.serialize_aws_json_1_0(
                value["definition"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdatePolicyInput:
    out: UpdatePolicyInput = {}  # type: ignore[typeddict-item]
    if "policyStoreId" in data:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("UpdatePolicyInput.policy_store_id required")
    if "policyId" in data:
        out["policy_id"] = data["policyId"]
    else:
        raise DeserializationError("UpdatePolicyInput.policy_id required")
    if "definition" in data:
        import aws_sdk_verifiedpermissions.types.update_policy_definition

        out["definition"] = (
            aws_sdk_verifiedpermissions.types.update_policy_definition.deserialize_aws_json_1_0(
                data["definition"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    return out
