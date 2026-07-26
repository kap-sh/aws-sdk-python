"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolVnfcResourceInfoMetadata``."""

from typing_extensions import NotRequired, TypedDict


class GetSolVnfcResourceInfoMetadata(TypedDict, closed=True):
    node_group: NotRequired["str"]
    """<p>Information about the node group.</p>"""
    cluster: NotRequired["str"]
    """<p>Information about the cluster.</p>"""
    helm_chart: NotRequired["str"]
    """<p>Information about the helm chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolVnfcResourceInfoMetadata) -> dict:
    out: dict = {}
    if "node_group" in value:
        out["nodeGroup"] = value["node_group"]
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    if "helm_chart" in value:
        out["helmChart"] = value["helm_chart"]
    return out


def deserialize_json(data: dict) -> GetSolVnfcResourceInfoMetadata:
    out: GetSolVnfcResourceInfoMetadata = {}  # type: ignore[typeddict-item]
    if "nodeGroup" in data:
        out["node_group"] = data["nodeGroup"]
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    if "helmChart" in data:
        out["helm_chart"] = data["helmChart"]
    return out
