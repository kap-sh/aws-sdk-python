"""Generated from Smithy shape ``com.amazonaws.kafka#DeleteVpcConnectionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.vpc_connection_state


class DeleteVpcConnectionResponse(TypedDict):
    vpc_connection_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies an MSK VPC connection.</p>"""
    state: NotRequired["aws_sdk_kafka.types.vpc_connection_state.VpcConnectionState"]
    """<p>The state of the VPC connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVpcConnectionResponse) -> dict:
    out: dict = {}
    if "vpc_connection_arn" in value:
        out["vpcConnectionArn"] = value["vpc_connection_arn"]
    if "state" in value:
        import aws_sdk_kafka.types.vpc_connection_state

        out["state"] = aws_sdk_kafka.types.vpc_connection_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> DeleteVpcConnectionResponse:
    out: DeleteVpcConnectionResponse = {}  # type: ignore[typeddict-item]
    if "vpcConnectionArn" in data:
        out["vpc_connection_arn"] = data["vpcConnectionArn"]
    if "state" in data:
        import aws_sdk_kafka.types.vpc_connection_state

        out["state"] = aws_sdk_kafka.types.vpc_connection_state.deserialize_json(
            data["state"]
        )
    return out
