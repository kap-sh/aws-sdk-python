"""Generated from Smithy shape ``com.amazonaws.fsx#S3AccessPointVpcConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.vpc_id


class S3AccessPointVpcConfiguration(TypedDict, closed=True):
    vpc_id: NotRequired["aws_sdk_fsx.types.vpc_id.VpcId"]
    """<p>Specifies the virtual private cloud (VPC) for the S3 access point VPC configuration, if one exists.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3AccessPointVpcConfiguration) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3AccessPointVpcConfiguration:
    out: S3AccessPointVpcConfiguration = {}  # type: ignore[typeddict-item]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    return out
