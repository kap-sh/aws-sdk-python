"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileManualAssignmentQueueConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.routing_profile_queue_reference


class RoutingProfileManualAssignmentQueueConfig(TypedDict, closed=True):
    queue_reference: "capo_connect.types.routing_profile_queue_reference.RoutingProfileQueueReference"


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileManualAssignmentQueueConfig) -> dict:
    out: dict = {}
    import capo_connect.types.routing_profile_queue_reference

    out["QueueReference"] = (
        capo_connect.types.routing_profile_queue_reference.serialize_json(
            value["queue_reference"]
        )
    )
    return out


def deserialize_json(data: dict) -> RoutingProfileManualAssignmentQueueConfig:
    out: RoutingProfileManualAssignmentQueueConfig = {}  # type: ignore[typeddict-item]
    if "QueueReference" in data:
        import capo_connect.types.routing_profile_queue_reference

        out["queue_reference"] = (
            capo_connect.types.routing_profile_queue_reference.deserialize_json(
                data["QueueReference"]
            )
        )
    else:
        raise DeserializationError(
            "RoutingProfileManualAssignmentQueueConfig.queue_reference required"
        )
    return out
