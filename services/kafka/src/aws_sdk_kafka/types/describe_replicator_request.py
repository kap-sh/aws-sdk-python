"""Generated from Smithy shape ``com.amazonaws.kafka#DescribeReplicatorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class DescribeReplicatorRequest(TypedDict, closed=True):
    replicator_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the replicator to be described.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeReplicatorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeReplicatorRequest:
    out: DescribeReplicatorRequest = {}  # type: ignore[typeddict-item]
    return out
