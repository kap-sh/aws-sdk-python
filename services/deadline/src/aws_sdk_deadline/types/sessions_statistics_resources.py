"""Generated from Smithy shape ``com.amazonaws.deadline#SessionsStatisticsResources``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.fleet_ids
    import aws_sdk_deadline.types.queue_ids


class _SessionsStatisticsResources_queueIds(TypedDict, closed=True):
    queueIds: "aws_sdk_deadline.types.queue_ids.QueueIds"


class _SessionsStatisticsResources_fleetIds(TypedDict, closed=True):
    fleetIds: "aws_sdk_deadline.types.fleet_ids.FleetIds"


SessionsStatisticsResources: TypeAlias = (
    _SessionsStatisticsResources_queueIds | _SessionsStatisticsResources_fleetIds
)


# --- restJson1 ser/de ---
def serialize_json(value: SessionsStatisticsResources) -> dict:
    if "queueIds" in value:
        import aws_sdk_deadline.types.queue_ids

        return {
            "queueIds": aws_sdk_deadline.types.queue_ids.serialize_json(
                value["queueIds"]
            )
        }
    elif "fleetIds" in value:
        import aws_sdk_deadline.types.fleet_ids

        return {
            "fleetIds": aws_sdk_deadline.types.fleet_ids.serialize_json(
                value["fleetIds"]
            )
        }
    else:
        raise SerializationError("SessionsStatisticsResources: no variant present")


def deserialize_json(data: dict) -> SessionsStatisticsResources:
    if "queueIds" in data:
        import aws_sdk_deadline.types.queue_ids

        return {
            "queueIds": aws_sdk_deadline.types.queue_ids.deserialize_json(
                data["queueIds"]
            )
        }
    elif "fleetIds" in data:
        import aws_sdk_deadline.types.fleet_ids

        return {
            "fleetIds": aws_sdk_deadline.types.fleet_ids.deserialize_json(
                data["fleetIds"]
            )
        }
    else:
        raise DeserializationError(
            "SessionsStatisticsResources: no recognized variant key"
        )
