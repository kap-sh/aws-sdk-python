"""Generated from Smithy shape ``com.amazonaws.emrcontainers#EksInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.kubernetes_namespace
    import aws_sdk_emr_containers.types.resource_name_string


class EksInfo(TypedDict):
    namespace: NotRequired[
        "aws_sdk_emr_containers.types.kubernetes_namespace.KubernetesNamespace"
    ]
    """<p>The namespaces of the Amazon EKS cluster.</p>"""
    node_label: NotRequired[
        "aws_sdk_emr_containers.types.resource_name_string.ResourceNameString"
    ]
    """<p>The nodeLabel of the nodes where the resources of this virtual cluster can get scheduled. It requires relevant scaling and policy engine addons.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksInfo) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "node_label" in value:
        out["nodeLabel"] = value["node_label"]
    return out


def deserialize_json(data: dict) -> EksInfo:
    out: EksInfo = {}  # type: ignore[typeddict-item]
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    if "nodeLabel" in data:
        out["node_label"] = data["nodeLabel"]
    return out
