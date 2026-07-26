"""Generated from Smithy shape ``com.amazonaws.emrcontainers#SecureNamespaceInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.cluster_id
    import capo_emr_containers.types.kubernetes_namespace


class SecureNamespaceInfo(TypedDict, closed=True):
    cluster_id: NotRequired["capo_emr_containers.types.cluster_id.ClusterId"]
    """<p>The ID of the Amazon EKS cluster where Amazon EMR on EKS jobs run.</p>"""
    namespace: NotRequired[
        "capo_emr_containers.types.kubernetes_namespace.KubernetesNamespace"
    ]
    """<p>The namespace of the Amazon EKS cluster where the system jobs run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecureNamespaceInfo) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["clusterId"] = value["cluster_id"]
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    return out


def deserialize_json(data: dict) -> SecureNamespaceInfo:
    out: SecureNamespaceInfo = {}  # type: ignore[typeddict-item]
    if "clusterId" in data:
        out["cluster_id"] = data["clusterId"]
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    return out
