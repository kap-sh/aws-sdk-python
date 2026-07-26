"""Generated from Smithy shape ``com.amazonaws.dlm#LifecyclePolicySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dlm.types.default_policy
    import capo_dlm.types.gettable_policy_state_values
    import capo_dlm.types.policy_description
    import capo_dlm.types.policy_id
    import capo_dlm.types.policy_type_values
    import capo_dlm.types.tag_map


class LifecyclePolicySummary(TypedDict, closed=True):
    policy_id: NotRequired["capo_dlm.types.policy_id.PolicyId"]
    """<p>The identifier of the lifecycle policy.</p>"""
    description: NotRequired["capo_dlm.types.policy_description.PolicyDescription"]
    """<p>The description of the lifecycle policy.</p>"""
    state: NotRequired[
        "capo_dlm.types.gettable_policy_state_values.GettablePolicyStateValues"
    ]
    """<p>The activation state of the lifecycle policy.</p>"""
    tags: NotRequired["capo_dlm.types.tag_map.TagMap"]
    """<p>The tags.</p>"""
    policy_type: NotRequired["capo_dlm.types.policy_type_values.PolicyTypeValues"]
    """<p>The type of policy. <code>EBS_SNAPSHOT_MANAGEMENT</code> indicates that the policy manages the lifecycle of Amazon EBS snapshots. <code>IMAGE_MANAGEMENT</code> indicates that the policy manages the lifecycle of EBS-backed AMIs. <code>EVENT_BASED_POLICY</code> indicates that the policy automates cross-account snapshot copies for snapshots that are shared with your account.</p>"""
    default_policy: NotRequired["capo_dlm.types.default_policy.DefaultPolicy"]
    """<p> <b>[Default policies only]</b> The type of default policy. Values include:</p> <ul> <li> <p> <code>VOLUME</code> - Default policy for EBS snapshots</p> </li> <li> <p> <code>INSTANCE</code> - Default policy for EBS-backed AMIs</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicySummary) -> dict:
    out: dict = {}
    if "policy_id" in value:
        out["PolicyId"] = value["policy_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "state" in value:
        import capo_dlm.types.gettable_policy_state_values

        out["State"] = capo_dlm.types.gettable_policy_state_values.serialize_json(
            value["state"]
        )
    if "tags" in value:
        import capo_dlm.types.tag_map

        out["Tags"] = capo_dlm.types.tag_map.serialize_json(value["tags"])
    if "policy_type" in value:
        import capo_dlm.types.policy_type_values

        out["PolicyType"] = capo_dlm.types.policy_type_values.serialize_json(
            value["policy_type"]
        )
    if "default_policy" in value:
        out["DefaultPolicy"] = value["default_policy"]
    return out


def deserialize_json(data: dict) -> LifecyclePolicySummary:
    out: LifecyclePolicySummary = {}  # type: ignore[typeddict-item]
    if "PolicyId" in data:
        out["policy_id"] = data["PolicyId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "State" in data:
        import capo_dlm.types.gettable_policy_state_values

        out["state"] = capo_dlm.types.gettable_policy_state_values.deserialize_json(
            data["State"]
        )
    if "Tags" in data:
        import capo_dlm.types.tag_map

        out["tags"] = capo_dlm.types.tag_map.deserialize_json(data["Tags"])
    if "PolicyType" in data:
        import capo_dlm.types.policy_type_values

        out["policy_type"] = capo_dlm.types.policy_type_values.deserialize_json(
            data["PolicyType"]
        )
    if "DefaultPolicy" in data:
        out["default_policy"] = data["DefaultPolicy"]
    return out
