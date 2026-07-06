"""Generated from Smithy shape ``com.amazonaws.costexplorer#ResourceUtilization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.ec2_resource_utilization


class ResourceUtilization(TypedDict, closed=True):
    ec2_resource_utilization: NotRequired[
        "aws_sdk_cost_explorer.types.ec2_resource_utilization.EC2ResourceUtilization"
    ]
    """<p>The utilization of current Amazon EC2 instance. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceUtilization) -> dict:
    out: dict = {}
    if "ec2_resource_utilization" in value:
        import aws_sdk_cost_explorer.types.ec2_resource_utilization

        out["EC2ResourceUtilization"] = (
            aws_sdk_cost_explorer.types.ec2_resource_utilization.serialize_aws_json_1_1(
                value["ec2_resource_utilization"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceUtilization:
    out: ResourceUtilization = {}  # type: ignore[typeddict-item]
    if "EC2ResourceUtilization" in data:
        import aws_sdk_cost_explorer.types.ec2_resource_utilization

        out["ec2_resource_utilization"] = (
            aws_sdk_cost_explorer.types.ec2_resource_utilization.deserialize_aws_json_1_1(
                data["EC2ResourceUtilization"]
            )
        )
    return out
