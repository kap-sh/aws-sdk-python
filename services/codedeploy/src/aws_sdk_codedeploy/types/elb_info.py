"""Generated from Smithy shape ``com.amazonaws.codedeploy#ELBInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.elb_name


class ELBInfo(TypedDict):
    name: NotRequired["aws_sdk_codedeploy.types.elb_name.ELBName"]
    """<p>For blue/green deployments, the name of the Classic Load Balancer that is used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the Classic Load Balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ELBInfo) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ELBInfo:
    out: ELBInfo = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    return out
