"""Generated from Smithy shape ``com.amazonaws.kafka#ReplicationStartingPosition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.replication_starting_position_type


class ReplicationStartingPosition(TypedDict):
    type: NotRequired[
        "aws_sdk_kafka.types.replication_starting_position_type.ReplicationStartingPositionType"
    ]
    """<p>The type of replication starting position.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationStartingPosition) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_kafka.types.replication_starting_position_type

        out["type"] = (
            aws_sdk_kafka.types.replication_starting_position_type.serialize_json(
                value["type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReplicationStartingPosition:
    out: ReplicationStartingPosition = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_kafka.types.replication_starting_position_type

        out["type"] = (
            aws_sdk_kafka.types.replication_starting_position_type.deserialize_json(
                data["type"]
            )
        )
    return out
