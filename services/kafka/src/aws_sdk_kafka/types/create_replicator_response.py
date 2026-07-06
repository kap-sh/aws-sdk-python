"""Generated from Smithy shape ``com.amazonaws.kafka#CreateReplicatorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.replicator_state


class CreateReplicatorResponse(TypedDict, closed=True):
    replicator_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the replicator.</p>"""
    replicator_name: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>Name of the replicator provided by the customer.</p>"""
    replicator_state: NotRequired[
        "aws_sdk_kafka.types.replicator_state.ReplicatorState"
    ]
    """<p>State of the replicator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateReplicatorResponse) -> dict:
    out: dict = {}
    if "replicator_arn" in value:
        out["replicatorArn"] = value["replicator_arn"]
    if "replicator_name" in value:
        out["replicatorName"] = value["replicator_name"]
    if "replicator_state" in value:
        import aws_sdk_kafka.types.replicator_state

        out["replicatorState"] = aws_sdk_kafka.types.replicator_state.serialize_json(
            value["replicator_state"]
        )
    return out


def deserialize_json(data: dict) -> CreateReplicatorResponse:
    out: CreateReplicatorResponse = {}  # type: ignore[typeddict-item]
    if "replicatorArn" in data:
        out["replicator_arn"] = data["replicatorArn"]
    if "replicatorName" in data:
        out["replicator_name"] = data["replicatorName"]
    if "replicatorState" in data:
        import aws_sdk_kafka.types.replicator_state

        out["replicator_state"] = aws_sdk_kafka.types.replicator_state.deserialize_json(
            data["replicatorState"]
        )
    return out
