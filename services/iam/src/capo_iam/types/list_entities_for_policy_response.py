"""Generated from Smithy shape ``com.amazonaws.iam#ListEntitiesForPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.boolean_type
    import capo_iam.types.policy_group_list_type
    import capo_iam.types.policy_role_list_type
    import capo_iam.types.policy_user_list_type
    import capo_iam.types.response_marker_type


class ListEntitiesForPolicyResponse(TypedDict, closed=True):
    policy_groups: NotRequired[
        "capo_iam.types.policy_group_list_type.PolicyGroupListType"
    ]
    """<p>A list of IAM groups that the policy is attached to.</p>"""
    policy_users: NotRequired["capo_iam.types.policy_user_list_type.PolicyUserListType"]
    """<p>A list of IAM users that the policy is attached to.</p>"""
    policy_roles: NotRequired["capo_iam.types.policy_role_list_type.PolicyRoleListType"]
    """<p>A list of IAM roles that the policy is attached to.</p>"""
    is_truncated: "capo_iam.types.boolean_type.booleanType"
    """<p>A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the <code>Marker</code> request parameter to retrieve more items. Note that IAM might return fewer than the <code>MaxItems</code> number of results even when there are more results available. We recommend that you check <code>IsTruncated</code> after every call to ensure that you receive all your results.</p>"""
    marker: NotRequired["capo_iam.types.response_marker_type.responseMarkerType"]
    """<p>When <code>IsTruncated</code> is <code>true</code>, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent pagination request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListEntitiesForPolicyResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "policy_groups" in value:
        import capo_iam.types.policy_group_list_type

        capo_iam.types.policy_group_list_type.serialize_query(
            value["policy_groups"], pairs, f"{key_prefix}PolicyGroups"
        )
    if "policy_users" in value:
        import capo_iam.types.policy_user_list_type

        capo_iam.types.policy_user_list_type.serialize_query(
            value["policy_users"], pairs, f"{key_prefix}PolicyUsers"
        )
    if "policy_roles" in value:
        import capo_iam.types.policy_role_list_type

        capo_iam.types.policy_role_list_type.serialize_query(
            value["policy_roles"], pairs, f"{key_prefix}PolicyRoles"
        )
    pairs.append(
        (
            f"{key_prefix}IsTruncated",
            "true" if value.get("is_truncated", False) else "false",
        )
    )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> ListEntitiesForPolicyResponse:
    out: ListEntitiesForPolicyResponse = {}  # type: ignore[typeddict-item]
    child_policy_groups = el.find("PolicyGroups")
    if child_policy_groups is not None:
        import capo_iam.types.policy_group_list_type

        out["policy_groups"] = capo_iam.types.policy_group_list_type.deserialize_query(
            child_policy_groups
        )
    child_policy_users = el.find("PolicyUsers")
    if child_policy_users is not None:
        import capo_iam.types.policy_user_list_type

        out["policy_users"] = capo_iam.types.policy_user_list_type.deserialize_query(
            child_policy_users
        )
    child_policy_roles = el.find("PolicyRoles")
    if child_policy_roles is not None:
        import capo_iam.types.policy_role_list_type

        out["policy_roles"] = capo_iam.types.policy_role_list_type.deserialize_query(
            child_policy_roles
        )
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        out["is_truncated"] = False
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
