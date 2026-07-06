"""Generated from Smithy shape ``com.amazonaws.guardduty#KubernetesRoleDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string


class KubernetesRoleDetails(TypedDict, closed=True):
    kind: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The kind of role. For this API, the value of <code>kind</code> will be <code>Role</code>.</p>"""
    name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The name of the Kubernetes role.</p>"""
    uid: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The unique identifier of the Kubernetes role name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesRoleDetails) -> dict:
    out: dict = {}
    if "kind" in value:
        out["kind"] = value["kind"]
    if "name" in value:
        out["name"] = value["name"]
    if "uid" in value:
        out["uid"] = value["uid"]
    return out


def deserialize_json(data: dict) -> KubernetesRoleDetails:
    out: KubernetesRoleDetails = {}  # type: ignore[typeddict-item]
    if "kind" in data:
        out["kind"] = data["kind"]
    if "name" in data:
        out["name"] = data["name"]
    if "uid" in data:
        out["uid"] = data["uid"]
    return out
