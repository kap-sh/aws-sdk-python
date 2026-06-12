"""Generated from Smithy shape ``com.amazonaws.kafka#DeleteReplicatorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class DeleteReplicatorRequest(TypedDict):
    current_version: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The current version of the replicator.</p>"""
    replicator_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the replicator to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteReplicatorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteReplicatorRequest:
    out: DeleteReplicatorRequest = {}  # type: ignore[typeddict-item]
    return out
