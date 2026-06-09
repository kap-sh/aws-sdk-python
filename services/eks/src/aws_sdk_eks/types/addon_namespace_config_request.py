"""Generated from Smithy shape ``com.amazonaws.eks#AddonNamespaceConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.namespace


class AddonNamespaceConfigRequest(TypedDict):
    namespace: NotRequired["aws_sdk_eks.types.namespace.namespace"]
    """<p>The name of the Kubernetes namespace to install the addon in. Must be a valid RFC 1123 DNS label.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddonNamespaceConfigRequest) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    return out


def deserialize_json(data: dict) -> AddonNamespaceConfigRequest:
    out: AddonNamespaceConfigRequest = {}  # type: ignore[typeddict-item]
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    return out
