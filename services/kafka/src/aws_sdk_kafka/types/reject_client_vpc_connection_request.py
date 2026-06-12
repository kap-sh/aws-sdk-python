"""Generated from Smithy shape ``com.amazonaws.kafka#RejectClientVpcConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class RejectClientVpcConnectionRequest(TypedDict):
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""
    vpc_connection_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The VPC connection ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RejectClientVpcConnectionRequest) -> dict:
    out: dict = {}
    if "vpc_connection_arn" in value:
        out["vpcConnectionArn"] = value["vpc_connection_arn"]
    return out


def deserialize_json(data: dict) -> RejectClientVpcConnectionRequest:
    out: RejectClientVpcConnectionRequest = {}  # type: ignore[typeddict-item]
    if "vpcConnectionArn" in data:
        out["vpc_connection_arn"] = data["vpcConnectionArn"]
    return out
