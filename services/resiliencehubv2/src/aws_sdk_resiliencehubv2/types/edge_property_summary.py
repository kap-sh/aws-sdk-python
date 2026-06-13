"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#EdgePropertySummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.topology_type


class EdgePropertySummary(TypedDict):
    topology_type: NotRequired[
        "aws_sdk_resiliencehubv2.types.topology_type.TopologyType"
    ]
    """<p>The topology type of the edge.</p>"""
    label: NotRequired["str"]
    """<p>Human-readable relationship description. Only present for LLM-inferred edges.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EdgePropertySummary) -> dict:
    out: dict = {}
    if "topology_type" in value:
        import aws_sdk_resiliencehubv2.types.topology_type

        out["topologyType"] = (
            aws_sdk_resiliencehubv2.types.topology_type.serialize_json(
                value["topology_type"]
            )
        )
    if "label" in value:
        out["label"] = value["label"]
    return out


def deserialize_json(data: dict) -> EdgePropertySummary:
    out: EdgePropertySummary = {}  # type: ignore[typeddict-item]
    if "topologyType" in data:
        import aws_sdk_resiliencehubv2.types.topology_type

        out["topology_type"] = (
            aws_sdk_resiliencehubv2.types.topology_type.deserialize_json(
                data["topologyType"]
            )
        )
    if "label" in data:
        out["label"] = data["label"]
    return out
