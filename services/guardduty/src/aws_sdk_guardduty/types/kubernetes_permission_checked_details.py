"""Generated from Smithy shape ``com.amazonaws.guardduty#KubernetesPermissionCheckedDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.boolean
    import aws_sdk_guardduty.types.string


class KubernetesPermissionCheckedDetails(TypedDict):
    verb: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The verb component of the Kubernetes API call. For example, when you check whether or not you have the permission to call the <code>CreatePod</code> API, the verb component will be <code>Create</code>.</p>"""
    resource: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The Kubernetes resource with which your Kubernetes API call will interact.</p>"""
    namespace: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The namespace where the Kubernetes API action will take place.</p>"""
    allowed: NotRequired["aws_sdk_guardduty.types.boolean.Boolean"]
    """<p>Information whether the user has the permission to call the Kubernetes API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesPermissionCheckedDetails) -> dict:
    out: dict = {}
    if "verb" in value:
        out["verb"] = value["verb"]
    if "resource" in value:
        out["resource"] = value["resource"]
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "allowed" in value:
        out["allowed"] = value["allowed"]
    return out


def deserialize_json(data: dict) -> KubernetesPermissionCheckedDetails:
    out: KubernetesPermissionCheckedDetails = {}  # type: ignore[typeddict-item]
    if "verb" in data:
        out["verb"] = data["verb"]
    if "resource" in data:
        out["resource"] = data["resource"]
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    if "allowed" in data:
        out["allowed"] = data["allowed"]
    return out
