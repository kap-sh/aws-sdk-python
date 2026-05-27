"""Generated from Smithy shape ``com.amazonaws.eks#AddonNamespaceConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.namespace


class AddonNamespaceConfigResponse(TypedDict):
    namespace: NotRequired["aws_sdk_eks.types.namespace.namespace"]
    """<p>The name of the Kubernetes namespace where the addon is installed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddonNamespaceConfigResponse) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    return out


def deserialize_json(data: dict) -> AddonNamespaceConfigResponse:
    out: AddonNamespaceConfigResponse = {}  # type: ignore[typeddict-item]
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    return out
