"""Generated from Smithy shape ``com.amazonaws.kafka#DeleteVpcConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.vpc_connection_state


class DeleteVpcConnectionResponse(TypedDict, closed=True):
    vpc_connection_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies an MSK VPC connection.</p>"""
    state: NotRequired["capo_kafka.types.vpc_connection_state.VpcConnectionState"]
    """<p>The state of the VPC connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVpcConnectionResponse) -> dict:
    out: dict = {}
    if "vpc_connection_arn" in value:
        out["vpcConnectionArn"] = value["vpc_connection_arn"]
    if "state" in value:
        import capo_kafka.types.vpc_connection_state

        out["state"] = capo_kafka.types.vpc_connection_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> DeleteVpcConnectionResponse:
    out: DeleteVpcConnectionResponse = {}  # type: ignore[typeddict-item]
    if "vpcConnectionArn" in data:
        out["vpc_connection_arn"] = data["vpcConnectionArn"]
    if "state" in data:
        import capo_kafka.types.vpc_connection_state

        out["state"] = capo_kafka.types.vpc_connection_state.deserialize_json(
            data["state"]
        )
    return out
