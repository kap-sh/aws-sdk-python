"""Generated from Smithy shape ``com.amazonaws.wafv2#ManagedRuleSetSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.entity_description
    import aws_sdk_wafv2.types.entity_id
    import aws_sdk_wafv2.types.entity_name
    import aws_sdk_wafv2.types.label_name
    import aws_sdk_wafv2.types.lock_token
    import aws_sdk_wafv2.types.resource_arn


class ManagedRuleSetSummary(TypedDict):
    name: NotRequired["aws_sdk_wafv2.types.entity_name.EntityName"]
    """<p>The name of the managed rule set. You use this, along with the rule set ID, to identify the rule set.</p> <p>This name is assigned to the corresponding managed rule group, which your customers can access and use. </p>"""
    id: NotRequired["aws_sdk_wafv2.types.entity_id.EntityId"]
    """<p>A unique identifier for the managed rule set. The ID is returned in the responses to commands like <code>list</code>. You provide it to operations like <code>get</code> and <code>update</code>.</p>"""
    description: NotRequired["aws_sdk_wafv2.types.entity_description.EntityDescription"]
    """<p>A description of the set that helps with identification. </p>"""
    lock_token: NotRequired["aws_sdk_wafv2.types.lock_token.LockToken"]
    """<p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>"""
    arn: NotRequired["aws_sdk_wafv2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the entity.</p>"""
    label_namespace: NotRequired["aws_sdk_wafv2.types.label_name.LabelName"]
    """<p>The label namespace prefix for the managed rule groups that are offered to customers from this managed rule set. All labels that are added by rules in the managed rule group have this prefix. </p> <ul> <li> <p>The syntax for the label namespace prefix for a managed rule group is the following: </p> <p> <code>awswaf:managed:<vendor>:<rule group name></code>:</p> </li> <li> <p>When a rule with a label matches a web request, WAF adds the fully qualified label to the request. A fully qualified label is made up of the label namespace from the rule group or web ACL where the rule is defined and the label from the rule, separated by a colon: </p> <p> <code><label namespace>:<label from rule></code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedRuleSetSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "lock_token" in value:
        out["LockToken"] = value["lock_token"]
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "label_namespace" in value:
        out["LabelNamespace"] = value["label_namespace"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedRuleSetSummary:
    out: ManagedRuleSetSummary = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "LockToken" in data:
        out["lock_token"] = data["LockToken"]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    if "LabelNamespace" in data:
        out["label_namespace"] = data["LabelNamespace"]
    return out
