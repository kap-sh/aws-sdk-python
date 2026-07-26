"""Generated from Smithy shape ``com.amazonaws.wafv2#WebACLSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.entity_description
    import capo_wafv2.types.entity_id
    import capo_wafv2.types.entity_name
    import capo_wafv2.types.lock_token
    import capo_wafv2.types.resource_arn


class WebACLSummary(TypedDict, closed=True):
    name: NotRequired["capo_wafv2.types.entity_name.EntityName"]
    """<p>The name of the web ACL. You cannot change the name of a web ACL after you create it.</p>"""
    id: NotRequired["capo_wafv2.types.entity_id.EntityId"]
    """<p>The unique identifier for the web ACL. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>"""
    description: NotRequired["capo_wafv2.types.entity_description.EntityDescription"]
    """<p>A description of the web ACL that helps with identification. </p>"""
    lock_token: NotRequired["capo_wafv2.types.lock_token.LockToken"]
    """<p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>"""
    arn: NotRequired["capo_wafv2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the entity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebACLSummary) -> dict:
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
    return out


def deserialize_aws_json_1_1(data: dict) -> WebACLSummary:
    out: WebACLSummary = {}  # type: ignore[typeddict-item]
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
    return out
