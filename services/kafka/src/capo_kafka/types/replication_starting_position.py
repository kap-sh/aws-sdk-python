"""Generated from Smithy shape ``com.amazonaws.kafka#ReplicationStartingPosition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.replication_starting_position_type


class ReplicationStartingPosition(TypedDict, closed=True):
    type: NotRequired[
        "capo_kafka.types.replication_starting_position_type.ReplicationStartingPositionType"
    ]
    """<p>The type of replication starting position.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationStartingPosition) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_kafka.types.replication_starting_position_type

        out["type"] = (
            capo_kafka.types.replication_starting_position_type.serialize_json(
                value["type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReplicationStartingPosition:
    out: ReplicationStartingPosition = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_kafka.types.replication_starting_position_type

        out["type"] = (
            capo_kafka.types.replication_starting_position_type.deserialize_json(
                data["type"]
            )
        )
    return out
