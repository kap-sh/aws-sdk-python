"""Generated from Smithy shape ``com.amazonaws.kafka#DeleteReplicatorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.replicator_state


class DeleteReplicatorResponse(TypedDict):
    replicator_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the replicator.</p>"""
    replicator_state: NotRequired[
        "aws_sdk_kafka.types.replicator_state.ReplicatorState"
    ]
    """<p>The state of the replicator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteReplicatorResponse) -> dict:
    out: dict = {}
    if "replicator_arn" in value:
        out["replicatorArn"] = value["replicator_arn"]
    if "replicator_state" in value:
        import aws_sdk_kafka.types.replicator_state

        out["replicatorState"] = aws_sdk_kafka.types.replicator_state.serialize_json(
            value["replicator_state"]
        )
    return out


def deserialize_json(data: dict) -> DeleteReplicatorResponse:
    out: DeleteReplicatorResponse = {}  # type: ignore[typeddict-item]
    if "replicatorArn" in data:
        out["replicator_arn"] = data["replicatorArn"]
    if "replicatorState" in data:
        import aws_sdk_kafka.types.replicator_state

        out["replicator_state"] = aws_sdk_kafka.types.replicator_state.deserialize_json(
            data["replicatorState"]
        )
    return out
