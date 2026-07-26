"""Generated from Smithy shape ``com.amazonaws.guardduty#KubernetesWorkload``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.container_uids
    import capo_guardduty.types.kubernetes_resources_types
    import capo_guardduty.types.string


class KubernetesWorkload(TypedDict, closed=True):
    container_uids: NotRequired["capo_guardduty.types.container_uids.ContainerUids"]
    """<p>A list of unique identifiers for the containers that are part of the Kubernetes workload.</p>"""
    namespace: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Kubernetes namespace in which the workload is running, providing logical isolation within the cluster.</p>"""
    kubernetes_resources_types: NotRequired[
        "capo_guardduty.types.kubernetes_resources_types.KubernetesResourcesTypes"
    ]
    """<p>The types of Kubernetes resources involved in the workload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesWorkload) -> dict:
    out: dict = {}
    if "container_uids" in value:
        import capo_guardduty.types.container_uids

        out["containerUids"] = capo_guardduty.types.container_uids.serialize_json(
            value["container_uids"]
        )
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "kubernetes_resources_types" in value:
        import capo_guardduty.types.kubernetes_resources_types

        out["type"] = capo_guardduty.types.kubernetes_resources_types.serialize_json(
            value["kubernetes_resources_types"]
        )
    return out


def deserialize_json(data: dict) -> KubernetesWorkload:
    out: KubernetesWorkload = {}  # type: ignore[typeddict-item]
    if "containerUids" in data:
        import capo_guardduty.types.container_uids

        out["container_uids"] = capo_guardduty.types.container_uids.deserialize_json(
            data["containerUids"]
        )
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    if "type" in data:
        import capo_guardduty.types.kubernetes_resources_types

        out["kubernetes_resources_types"] = (
            capo_guardduty.types.kubernetes_resources_types.deserialize_json(
                data["type"]
            )
        )
    return out
