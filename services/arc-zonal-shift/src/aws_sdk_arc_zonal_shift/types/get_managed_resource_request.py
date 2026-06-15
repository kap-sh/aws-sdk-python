"""Generated from Smithy shape ``com.amazonaws.arczonalshift#GetManagedResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.resource_identifier


class GetManagedResourceRequest(TypedDict):
    resource_identifier: (
        "aws_sdk_arc_zonal_shift.types.resource_identifier.ResourceIdentifier"
    )
    r"""<p>The identifier for the resource that Amazon Web Services shifts traffic for. The identifier is the Amazon Resource Name (ARN) for the resource.</p> <p>Amazon Application Recovery Controller currently supports enabling the following resources for zonal shift and zonal autoshift:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.ec2-auto-scaling-groups.html\">Amazon EC2 Auto Scaling groups</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.eks.html\">Amazon Elastic Kubernetes Service</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.app-load-balancers.html\">Application Load Balancer</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.network-load-balancers.html\">Network Load Balancer</a> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetManagedResourceRequest:
    out: GetManagedResourceRequest = {}  # type: ignore[typeddict-item]
    return out
