"""Generated from Smithy shape ``com.amazonaws.networkmanager#EdgeOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.edge_set_list


class EdgeOverride(TypedDict, closed=True):
    edge_sets: NotRequired["aws_sdk_networkmanager.types.edge_set_list.EdgeSetList"]
    """<p>The list of edge locations.</p>"""
    use_edge: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The edge that should be used when overriding the current edge order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EdgeOverride) -> dict:
    out: dict = {}
    if "edge_sets" in value:
        import aws_sdk_networkmanager.types.edge_set_list

        out["EdgeSets"] = aws_sdk_networkmanager.types.edge_set_list.serialize_json(
            value["edge_sets"]
        )
    if "use_edge" in value:
        out["UseEdge"] = value["use_edge"]
    return out


def deserialize_json(data: dict) -> EdgeOverride:
    out: EdgeOverride = {}  # type: ignore[typeddict-item]
    if "EdgeSets" in data:
        import aws_sdk_networkmanager.types.edge_set_list

        out["edge_sets"] = aws_sdk_networkmanager.types.edge_set_list.deserialize_json(
            data["EdgeSets"]
        )
    if "UseEdge" in data:
        out["use_edge"] = data["UseEdge"]
    return out
