"""Generated from Smithy shape ``com.amazonaws.eks#CreateNodegroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.nodegroup


class CreateNodegroupResponse(TypedDict):
    nodegroup: NotRequired["aws_sdk_eks.types.nodegroup.Nodegroup"]
    """<p>The full description of your new node group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNodegroupResponse) -> dict:
    out: dict = {}
    if "nodegroup" in value:
        import aws_sdk_eks.types.nodegroup

        out["nodegroup"] = aws_sdk_eks.types.nodegroup.serialize_json(
            value["nodegroup"]
        )
    return out


def deserialize_json(data: dict) -> CreateNodegroupResponse:
    out: CreateNodegroupResponse = {}  # type: ignore[typeddict-item]
    if "nodegroup" in data:
        import aws_sdk_eks.types.nodegroup

        out["nodegroup"] = aws_sdk_eks.types.nodegroup.deserialize_json(
            data["nodegroup"]
        )
    return out
