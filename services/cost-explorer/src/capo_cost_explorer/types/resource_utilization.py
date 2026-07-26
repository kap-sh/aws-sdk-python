"""Generated from Smithy shape ``com.amazonaws.costexplorer#ResourceUtilization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.ec2_resource_utilization


class ResourceUtilization(TypedDict, closed=True):
    ec2_resource_utilization: NotRequired[
        "capo_cost_explorer.types.ec2_resource_utilization.EC2ResourceUtilization"
    ]
    """<p>The utilization of current Amazon EC2 instance. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceUtilization) -> dict:
    out: dict = {}
    if "ec2_resource_utilization" in value:
        import capo_cost_explorer.types.ec2_resource_utilization

        out["EC2ResourceUtilization"] = (
            capo_cost_explorer.types.ec2_resource_utilization.serialize_aws_json_1_1(
                value["ec2_resource_utilization"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceUtilization:
    out: ResourceUtilization = {}  # type: ignore[typeddict-item]
    if "EC2ResourceUtilization" in data:
        import capo_cost_explorer.types.ec2_resource_utilization

        out["ec2_resource_utilization"] = (
            capo_cost_explorer.types.ec2_resource_utilization.deserialize_aws_json_1_1(
                data["EC2ResourceUtilization"]
            )
        )
    return out
