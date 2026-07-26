"""Generated from Smithy shape ``com.amazonaws.eks#DescribeNodegroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.nodegroup


class DescribeNodegroupResponse(TypedDict, closed=True):
    nodegroup: NotRequired["capo_eks.types.nodegroup.Nodegroup"]
    """<p>The full description of your node group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeNodegroupResponse) -> dict:
    out: dict = {}
    if "nodegroup" in value:
        import capo_eks.types.nodegroup

        out["nodegroup"] = capo_eks.types.nodegroup.serialize_json(value["nodegroup"])
    return out


def deserialize_json(data: dict) -> DescribeNodegroupResponse:
    out: DescribeNodegroupResponse = {}  # type: ignore[typeddict-item]
    if "nodegroup" in data:
        import capo_eks.types.nodegroup

        out["nodegroup"] = capo_eks.types.nodegroup.deserialize_json(data["nodegroup"])
    return out
