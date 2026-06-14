"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#UpdatePolicyTemplateInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.policy_statement
    import aws_sdk_verifiedpermissions.types.policy_store_id
    import aws_sdk_verifiedpermissions.types.policy_template_description
    import aws_sdk_verifiedpermissions.types.policy_template_id
    import aws_sdk_verifiedpermissions.types.policy_template_name


class UpdatePolicyTemplateInput(TypedDict):
    policy_store_id: "aws_sdk_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    r"""<p>Specifies the ID of the policy store that contains the policy template that you want to update.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html\">ListPolicyStoreAliases</a>.</p>"""
    policy_template_id: (
        "aws_sdk_verifiedpermissions.types.policy_template_id.PolicyTemplateId"
    )
    """<p>Specifies the ID of the policy template that you want to update.</p> <p>You can use the policy template name in place of the policy template ID. When using a name, prefix it with <code>name/</code>. For example:</p> <ul> <li> <p>ID: <code>PTEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Name: <code>name/example-policy-template</code> </p> </li> </ul>"""
    description: NotRequired[
        "aws_sdk_verifiedpermissions.types.policy_template_description.PolicyTemplateDescription"
    ]
    """<p>Specifies a new description to apply to the policy template.</p>"""
    statement: "aws_sdk_verifiedpermissions.types.policy_statement.PolicyStatement"
    """<p>Specifies new statement content written in Cedar policy language to replace the current body of the policy template.</p> <p>You can change only the following elements of the policy body:</p> <ul> <li> <p>The <code>action</code> referenced by the policy template.</p> </li> <li> <p>Any conditional clauses, such as <code>when</code> or <code>unless</code> clauses.</p> </li> </ul> <p>You <b>can't</b> change the following elements:</p> <ul> <li> <p>The effect (<code>permit</code> or <code>forbid</code>) of the policy template.</p> </li> <li> <p>The <code>principal</code> referenced by the policy template.</p> </li> <li> <p>The <code>resource</code> referenced by the policy template.</p> </li> </ul>"""
    name: NotRequired[
        "aws_sdk_verifiedpermissions.types.policy_template_name.PolicyTemplateName"
    ]
    r"""<p>Specifies a name for the policy template that is unique among all policy templates within the policy store. You can use the name in place of the policy template ID in API operations that reference the policy template. The name must be prefixed with <code>name/</code>.</p> <note> <p>If you don't include the name in an update request, the existing name is unchanged. To remove a name, set it to an empty string (<code>\"\"</code>).</p> </note> <p>If you specify a name that is already associated with another policy template in the policy store, you receive a <code>ConflictException</code> error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdatePolicyTemplateInput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    out["policyTemplateId"] = value["policy_template_id"]
    if "description" in value:
        out["description"] = value["description"]
    out["statement"] = value["statement"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdatePolicyTemplateInput:
    out: UpdatePolicyTemplateInput = {}  # type: ignore[typeddict-item]
    if "policyStoreId" in data:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("UpdatePolicyTemplateInput.policy_store_id required")
    if "policyTemplateId" in data:
        out["policy_template_id"] = data["policyTemplateId"]
    else:
        raise DeserializationError(
            "UpdatePolicyTemplateInput.policy_template_id required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "statement" in data:
        out["statement"] = data["statement"]
    else:
        raise DeserializationError("UpdatePolicyTemplateInput.statement required")
    if "name" in data:
        out["name"] = data["name"]
    return out
