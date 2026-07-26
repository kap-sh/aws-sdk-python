"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#InternalAccessDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.action_list
    import capo_accessanalyzer.types.condition_key_map
    import capo_accessanalyzer.types.finding_source_list
    import capo_accessanalyzer.types.internal_access_type
    import capo_accessanalyzer.types.principal_map
    import capo_accessanalyzer.types.principal_type
    import capo_accessanalyzer.types.resource_control_policy_restriction
    import capo_accessanalyzer.types.service_control_policy_restriction


class InternalAccessDetails(TypedDict, closed=True):
    action: NotRequired["capo_accessanalyzer.types.action_list.ActionList"]
    """<p>The action in the analyzed policy statement that has internal access permission to use.</p>"""
    condition: NotRequired[
        "capo_accessanalyzer.types.condition_key_map.ConditionKeyMap"
    ]
    """<p>The condition in the analyzed policy statement that resulted in an internal access finding.</p>"""
    principal: NotRequired["capo_accessanalyzer.types.principal_map.PrincipalMap"]
    """<p>The principal that has access to a resource within the internal environment.</p>"""
    principal_owner_account: NotRequired["str"]
    """<p>The Amazon Web Services account ID that owns the principal identified in the internal access finding.</p>"""
    access_type: NotRequired[
        "capo_accessanalyzer.types.internal_access_type.InternalAccessType"
    ]
    """<p>The type of internal access identified in the finding. This indicates how the access is granted within your Amazon Web Services environment.</p>"""
    principal_type: NotRequired[
        "capo_accessanalyzer.types.principal_type.PrincipalType"
    ]
    """<p>The type of principal identified in the internal access finding, such as IAM role or IAM user.</p>"""
    sources: NotRequired[
        "capo_accessanalyzer.types.finding_source_list.FindingSourceList"
    ]
    """<p>The sources of the internal access finding. This indicates how the access that generated the finding is granted within your Amazon Web Services environment.</p>"""
    resource_control_policy_restriction: NotRequired[
        "capo_accessanalyzer.types.resource_control_policy_restriction.ResourceControlPolicyRestriction"
    ]
    """<p>The type of restriction applied to the finding by the resource owner with an Organizations resource control policy (RCP).</p> <ul> <li> <p> <code>APPLICABLE</code>: There is an RCP present in the organization but IAM Access Analyzer does not include it in the evaluation of effective permissions. For example, if <code>s3:DeleteObject</code> is blocked by the RCP and the restriction is <code>APPLICABLE</code>, then <code>s3:DeleteObject</code> would still be included in the list of actions for the finding. Only applicable to internal access findings with the account as the zone of trust. </p> </li> <li> <p> <code>FAILED_TO_EVALUATE_RCP</code>: There was an error evaluating the RCP.</p> </li> <li> <p> <code>NOT_APPLICABLE</code>: There was no RCP present in the organization. For internal access findings with the account as the zone of trust, <code>NOT_APPLICABLE</code> could also indicate that there was no RCP applicable to the resource.</p> </li> <li> <p> <code>APPLIED</code>: An RCP is present in the organization and IAM Access Analyzer included it in the evaluation of effective permissions. For example, if <code>s3:DeleteObject</code> is blocked by the RCP and the restriction is <code>APPLIED</code>, then <code>s3:DeleteObject</code> would not be included in the list of actions for the finding. Only applicable to internal access findings with the organization as the zone of trust. </p> </li> </ul>"""
    service_control_policy_restriction: NotRequired[
        "capo_accessanalyzer.types.service_control_policy_restriction.ServiceControlPolicyRestriction"
    ]
    """<p>The type of restriction applied to the finding by an Organizations service control policy (SCP).</p> <ul> <li> <p> <code>APPLICABLE</code>: There is an SCP present in the organization but IAM Access Analyzer does not include it in the evaluation of effective permissions. Only applicable to internal access findings with the account as the zone of trust. </p> </li> <li> <p> <code>FAILED_TO_EVALUATE_SCP</code>: There was an error evaluating the SCP.</p> </li> <li> <p> <code>NOT_APPLICABLE</code>: There was no SCP present in the organization. For internal access findings with the account as the zone of trust, <code>NOT_APPLICABLE</code> could also indicate that there was no SCP applicable to the principal.</p> </li> <li> <p> <code>APPLIED</code>: An SCP is present in the organization and IAM Access Analyzer included it in the evaluation of effective permissions. Only applicable to internal access findings with the organization as the zone of trust. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalAccessDetails) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_accessanalyzer.types.action_list

        out["action"] = capo_accessanalyzer.types.action_list.serialize_json(
            value["action"]
        )
    if "condition" in value:
        import capo_accessanalyzer.types.condition_key_map

        out["condition"] = capo_accessanalyzer.types.condition_key_map.serialize_json(
            value["condition"]
        )
    if "principal" in value:
        import capo_accessanalyzer.types.principal_map

        out["principal"] = capo_accessanalyzer.types.principal_map.serialize_json(
            value["principal"]
        )
    if "principal_owner_account" in value:
        out["principalOwnerAccount"] = value["principal_owner_account"]
    if "access_type" in value:
        out["accessType"] = value["access_type"]
    if "principal_type" in value:
        out["principalType"] = value["principal_type"]
    if "sources" in value:
        import capo_accessanalyzer.types.finding_source_list

        out["sources"] = capo_accessanalyzer.types.finding_source_list.serialize_json(
            value["sources"]
        )
    if "resource_control_policy_restriction" in value:
        out["resourceControlPolicyRestriction"] = value[
            "resource_control_policy_restriction"
        ]
    if "service_control_policy_restriction" in value:
        out["serviceControlPolicyRestriction"] = value[
            "service_control_policy_restriction"
        ]
    return out


def deserialize_json(data: dict) -> InternalAccessDetails:
    out: InternalAccessDetails = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import capo_accessanalyzer.types.action_list

        out["action"] = capo_accessanalyzer.types.action_list.deserialize_json(
            data["action"]
        )
    if "condition" in data:
        import capo_accessanalyzer.types.condition_key_map

        out["condition"] = capo_accessanalyzer.types.condition_key_map.deserialize_json(
            data["condition"]
        )
    if "principal" in data:
        import capo_accessanalyzer.types.principal_map

        out["principal"] = capo_accessanalyzer.types.principal_map.deserialize_json(
            data["principal"]
        )
    if "principalOwnerAccount" in data:
        out["principal_owner_account"] = data["principalOwnerAccount"]
    if "accessType" in data:
        out["access_type"] = data["accessType"]
    if "principalType" in data:
        out["principal_type"] = data["principalType"]
    if "sources" in data:
        import capo_accessanalyzer.types.finding_source_list

        out["sources"] = capo_accessanalyzer.types.finding_source_list.deserialize_json(
            data["sources"]
        )
    if "resourceControlPolicyRestriction" in data:
        out["resource_control_policy_restriction"] = data[
            "resourceControlPolicyRestriction"
        ]
    if "serviceControlPolicyRestriction" in data:
        out["service_control_policy_restriction"] = data[
            "serviceControlPolicyRestriction"
        ]
    return out
