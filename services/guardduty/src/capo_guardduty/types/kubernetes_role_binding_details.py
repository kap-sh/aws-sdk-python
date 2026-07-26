"""Generated from Smithy shape ``com.amazonaws.guardduty#KubernetesRoleBindingDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class KubernetesRoleBindingDetails(TypedDict, closed=True):
    kind: NotRequired["capo_guardduty.types.string.String"]
    """<p>The kind of the role. For role binding, this value will be <code>RoleBinding</code>.</p>"""
    name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the <code>RoleBinding</code>.</p>"""
    uid: NotRequired["capo_guardduty.types.string.String"]
    """<p>The unique identifier of the role binding.</p>"""
    role_ref_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the role being referenced. This must match the name of the <code>Role</code> or <code>ClusterRole</code> that you want to bind to.</p>"""
    role_ref_kind: NotRequired["capo_guardduty.types.string.String"]
    """<p>The type of the role being referenced. This could be either <code>Role</code> or <code>ClusterRole</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesRoleBindingDetails) -> dict:
    out: dict = {}
    if "kind" in value:
        out["kind"] = value["kind"]
    if "name" in value:
        out["name"] = value["name"]
    if "uid" in value:
        out["uid"] = value["uid"]
    if "role_ref_name" in value:
        out["roleRefName"] = value["role_ref_name"]
    if "role_ref_kind" in value:
        out["roleRefKind"] = value["role_ref_kind"]
    return out


def deserialize_json(data: dict) -> KubernetesRoleBindingDetails:
    out: KubernetesRoleBindingDetails = {}  # type: ignore[typeddict-item]
    if "kind" in data:
        out["kind"] = data["kind"]
    if "name" in data:
        out["name"] = data["name"]
    if "uid" in data:
        out["uid"] = data["uid"]
    if "roleRefName" in data:
        out["role_ref_name"] = data["roleRefName"]
    if "roleRefKind" in data:
        out["role_ref_kind"] = data["roleRefKind"]
    return out
