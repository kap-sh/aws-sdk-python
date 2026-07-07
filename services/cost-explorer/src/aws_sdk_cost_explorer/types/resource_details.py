"""Generated from Smithy shape ``com.amazonaws.costexplorer#ResourceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.ec2_resource_details


class ResourceDetails(TypedDict, closed=True):
    ec2_resource_details: NotRequired[
        "aws_sdk_cost_explorer.types.ec2_resource_details.EC2ResourceDetails"
    ]
    """<p>Details for the Amazon EC2 resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDetails) -> dict:
    out: dict = {}
    if "ec2_resource_details" in value:
        import aws_sdk_cost_explorer.types.ec2_resource_details

        out["EC2ResourceDetails"] = (
            aws_sdk_cost_explorer.types.ec2_resource_details.serialize_aws_json_1_1(
                value["ec2_resource_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceDetails:
    out: ResourceDetails = {}  # type: ignore[typeddict-item]
    if "EC2ResourceDetails" in data:
        import aws_sdk_cost_explorer.types.ec2_resource_details

        out["ec2_resource_details"] = (
            aws_sdk_cost_explorer.types.ec2_resource_details.deserialize_aws_json_1_1(
                data["EC2ResourceDetails"]
            )
        )
    return out
