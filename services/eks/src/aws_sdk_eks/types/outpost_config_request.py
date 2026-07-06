"""Generated from Smithy shape ``com.amazonaws.eks#OutpostConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_eks.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eks.types.control_plane_placement_request
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.string_list


class OutpostConfigRequest(TypedDict, closed=True):
    outpost_arns: "aws_sdk_eks.types.string_list.StringList"
    """<p>The ARN of the Outpost that you want to use for your local Amazon EKS cluster on Outposts. Only a single Outpost ARN is supported.</p>"""
    control_plane_instance_type: "aws_sdk_eks.types.string.String"
    r"""<p>The Amazon EC2 instance type that you want to use for your local Amazon EKS cluster on Outposts. Choose an instance type based on the number of nodes that your cluster will have. For more information, see <a href=\"https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html\">Capacity considerations</a> in the <i>Amazon EKS User Guide</i>.</p> <p>The instance type that you specify is used for all Kubernetes control plane instances. The instance type can't be changed after cluster creation. The control plane is not automatically scaled by Amazon EKS.</p> <p> </p>"""
    control_plane_placement: NotRequired[
        "aws_sdk_eks.types.control_plane_placement_request.ControlPlanePlacementRequest"
    ]
    r"""<p>An object representing the placement configuration for all the control plane instances of your local Amazon EKS cluster on an Amazon Web Services Outpost. For more information, see <a href=\"https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html\">Capacity considerations</a> in the <i>Amazon EKS User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutpostConfigRequest) -> dict:
    out: dict = {}
    import aws_sdk_eks.types.string_list

    out["outpostArns"] = aws_sdk_eks.types.string_list.serialize_json(
        value["outpost_arns"]
    )
    out["controlPlaneInstanceType"] = value["control_plane_instance_type"]
    if "control_plane_placement" in value:
        import aws_sdk_eks.types.control_plane_placement_request

        out["controlPlanePlacement"] = (
            aws_sdk_eks.types.control_plane_placement_request.serialize_json(
                value["control_plane_placement"]
            )
        )
    return out


def deserialize_json(data: dict) -> OutpostConfigRequest:
    out: OutpostConfigRequest = {}  # type: ignore[typeddict-item]
    if "outpostArns" in data:
        import aws_sdk_eks.types.string_list

        out["outpost_arns"] = aws_sdk_eks.types.string_list.deserialize_json(
            data["outpostArns"]
        )
    else:
        raise DeserializationError("OutpostConfigRequest.outpost_arns required")
    if "controlPlaneInstanceType" in data:
        out["control_plane_instance_type"] = data["controlPlaneInstanceType"]
    else:
        raise DeserializationError(
            "OutpostConfigRequest.control_plane_instance_type required"
        )
    if "controlPlanePlacement" in data:
        import aws_sdk_eks.types.control_plane_placement_request

        out["control_plane_placement"] = (
            aws_sdk_eks.types.control_plane_placement_request.deserialize_json(
                data["controlPlanePlacement"]
            )
        )
    return out
