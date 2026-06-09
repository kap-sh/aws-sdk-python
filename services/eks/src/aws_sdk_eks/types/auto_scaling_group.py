"""Generated from Smithy shape ``com.amazonaws.eks#AutoScalingGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class AutoScalingGroup(TypedDict):
    name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The name of the Auto Scaling group associated with an Amazon EKS managed node group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoScalingGroup) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AutoScalingGroup:
    out: AutoScalingGroup = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    return out
