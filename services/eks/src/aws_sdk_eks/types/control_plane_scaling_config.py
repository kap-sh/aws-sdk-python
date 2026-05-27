"""Generated from Smithy shape ``com.amazonaws.eks#ControlPlaneScalingConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.provisioned_control_plane_tier


class ControlPlaneScalingConfig(TypedDict):
    tier: NotRequired[
        "aws_sdk_eks.types.provisioned_control_plane_tier.ProvisionedControlPlaneTier"
    ]
    """<p>The control plane scaling tier configuration. Available options are <code>standard</code>, <code>tier-xl</code>, <code>tier-2xl</code>, <code>tier-4xl, or tier-8xl</code>. For more information, see EKS Provisioned Control Plane in the Amazon EKS User Guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlPlaneScalingConfig) -> dict:
    out: dict = {}
    if "tier" in value:
        import aws_sdk_eks.types.provisioned_control_plane_tier

        out["tier"] = aws_sdk_eks.types.provisioned_control_plane_tier.serialize_json(
            value["tier"]
        )
    return out


def deserialize_json(data: dict) -> ControlPlaneScalingConfig:
    out: ControlPlaneScalingConfig = {}  # type: ignore[typeddict-item]
    if "tier" in data:
        import aws_sdk_eks.types.provisioned_control_plane_tier

        out["tier"] = aws_sdk_eks.types.provisioned_control_plane_tier.deserialize_json(
            data["tier"]
        )
    return out
