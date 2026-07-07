"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#KubernetesScalingResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.kubernetes_namespace


class KubernetesScalingResource(TypedDict, closed=True):
    namespace: (
        "aws_sdk_arc_region_switch.types.kubernetes_namespace.KubernetesNamespace"
    )
    """<p>The namespace for the Kubernetes resource.</p>"""
    name: "str"
    """<p>The name for the Kubernetes resource.</p>"""
    hpa_name: NotRequired["str"]
    """<p>The hpaname for the Kubernetes resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KubernetesScalingResource) -> dict:
    out: dict = {}
    out["namespace"] = value["namespace"]
    out["name"] = value["name"]
    if "hpa_name" in value:
        out["hpaName"] = value["hpa_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> KubernetesScalingResource:
    out: KubernetesScalingResource = {}  # type: ignore[typeddict-item]
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    else:
        raise DeserializationError("KubernetesScalingResource.namespace required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("KubernetesScalingResource.name required")
    if "hpaName" in data:
        out["hpa_name"] = data["hpaName"]
    return out
