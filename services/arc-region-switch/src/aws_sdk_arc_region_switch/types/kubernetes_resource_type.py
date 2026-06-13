"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#KubernetesResourceType``."""

from typing import TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError


class KubernetesResourceType(TypedDict):
    api_version: "str"
    """<p>The API version type for the Kubernetes resource.</p>"""
    kind: "str"
    """<p>The kind for the Kubernetes resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KubernetesResourceType) -> dict:
    out: dict = {}
    out["apiVersion"] = value["api_version"]
    out["kind"] = value["kind"]
    return out


def deserialize_aws_json_1_0(data: dict) -> KubernetesResourceType:
    out: KubernetesResourceType = {}  # type: ignore[typeddict-item]
    if "apiVersion" in data:
        out["api_version"] = data["apiVersion"]
    else:
        raise DeserializationError("KubernetesResourceType.api_version required")
    if "kind" in data:
        out["kind"] = data["kind"]
    else:
        raise DeserializationError("KubernetesResourceType.kind required")
    return out
