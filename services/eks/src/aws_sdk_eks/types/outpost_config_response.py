"""Generated from Smithy shape ``com.amazonaws.eks#OutpostConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_eks.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eks.types.control_plane_placement_response
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.string_list


class OutpostConfigResponse(TypedDict):
    outpost_arns: "aws_sdk_eks.types.string_list.StringList"
    """<p>The ARN of the Outpost that you specified for use with your local Amazon EKS cluster on Outposts.</p>"""
    control_plane_instance_type: "aws_sdk_eks.types.string.String"
    """<p>The Amazon EC2 instance type used for the control plane. The instance type is the same for all control plane instances.</p>"""
    control_plane_placement: NotRequired[
        "aws_sdk_eks.types.control_plane_placement_response.ControlPlanePlacementResponse"
    ]
    r"""<p>An object representing the placement configuration for all the control plane instances of your local Amazon EKS cluster on an Amazon Web Services Outpost. For more information, see <a href=\"https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html\">Capacity considerations</a> in the <i>Amazon EKS User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutpostConfigResponse) -> dict:
    out: dict = {}
    import aws_sdk_eks.types.string_list

    out["outpostArns"] = aws_sdk_eks.types.string_list.serialize_json(
        value["outpost_arns"]
    )
    out["controlPlaneInstanceType"] = value["control_plane_instance_type"]
    if "control_plane_placement" in value:
        import aws_sdk_eks.types.control_plane_placement_response

        out["controlPlanePlacement"] = (
            aws_sdk_eks.types.control_plane_placement_response.serialize_json(
                value["control_plane_placement"]
            )
        )
    return out


def deserialize_json(data: dict) -> OutpostConfigResponse:
    out: OutpostConfigResponse = {}  # type: ignore[typeddict-item]
    if "outpostArns" in data:
        import aws_sdk_eks.types.string_list

        out["outpost_arns"] = aws_sdk_eks.types.string_list.deserialize_json(
            data["outpostArns"]
        )
    else:
        raise DeserializationError("OutpostConfigResponse.outpost_arns required")
    if "controlPlaneInstanceType" in data:
        out["control_plane_instance_type"] = data["controlPlaneInstanceType"]
    else:
        raise DeserializationError(
            "OutpostConfigResponse.control_plane_instance_type required"
        )
    if "controlPlanePlacement" in data:
        import aws_sdk_eks.types.control_plane_placement_response

        out["control_plane_placement"] = (
            aws_sdk_eks.types.control_plane_placement_response.deserialize_json(
                data["controlPlanePlacement"]
            )
        )
    return out
