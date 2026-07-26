"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_supplychain.types.data_integration_event_dataset_target_details
    import capo_supplychain.types.data_integration_event_group_id
    import capo_supplychain.types.data_integration_event_type
    import capo_supplychain.types.uuid


class DataIntegrationEvent(TypedDict, closed=True):
    instance_id: "capo_supplychain.types.uuid.UUID"
    """<p>The AWS Supply Chain instance identifier.</p>"""
    event_id: "capo_supplychain.types.uuid.UUID"
    """<p>The unique event identifier.</p>"""
    event_type: (
        "capo_supplychain.types.data_integration_event_type.DataIntegrationEventType"
    )
    """<p>The data event type.</p>"""
    event_group_id: "capo_supplychain.types.data_integration_event_group_id.DataIntegrationEventGroupId"
    """<p>Event identifier (for example, orderId for InboundOrder) used for data sharding or partitioning.</p>"""
    event_timestamp: "datetime.datetime"
    """<p>The event timestamp (in epoch seconds).</p>"""
    dataset_target_details: NotRequired[
        "capo_supplychain.types.data_integration_event_dataset_target_details.DataIntegrationEventDatasetTargetDetails"
    ]
    """<p>The target dataset details for a DATASET event type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationEvent) -> dict:
    out: dict = {}
    out["instanceId"] = value["instance_id"]
    out["eventId"] = value["event_id"]
    import capo_supplychain.types.data_integration_event_type

    out["eventType"] = (
        capo_supplychain.types.data_integration_event_type.serialize_json(
            value["event_type"]
        )
    )
    out["eventGroupId"] = value["event_group_id"]
    import capo_supplychain.types._prelude.timestamp

    out["eventTimestamp"] = capo_supplychain.types._prelude.timestamp.serialize_json(
        value["event_timestamp"]
    )
    if "dataset_target_details" in value:
        import capo_supplychain.types.data_integration_event_dataset_target_details

        out["datasetTargetDetails"] = (
            capo_supplychain.types.data_integration_event_dataset_target_details.serialize_json(
                value["dataset_target_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataIntegrationEvent:
    out: DataIntegrationEvent = {}  # type: ignore[typeddict-item]
    if "instanceId" in data:
        out["instance_id"] = data["instanceId"]
    else:
        raise DeserializationError("DataIntegrationEvent.instance_id required")
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    else:
        raise DeserializationError("DataIntegrationEvent.event_id required")
    if "eventType" in data:
        import capo_supplychain.types.data_integration_event_type

        out["event_type"] = (
            capo_supplychain.types.data_integration_event_type.deserialize_json(
                data["eventType"]
            )
        )
    else:
        raise DeserializationError("DataIntegrationEvent.event_type required")
    if "eventGroupId" in data:
        out["event_group_id"] = data["eventGroupId"]
    else:
        raise DeserializationError("DataIntegrationEvent.event_group_id required")
    if "eventTimestamp" in data:
        import capo_supplychain.types._prelude.timestamp

        out["event_timestamp"] = (
            capo_supplychain.types._prelude.timestamp.deserialize_json(
                data["eventTimestamp"]
            )
        )
    else:
        raise DeserializationError("DataIntegrationEvent.event_timestamp required")
    if "datasetTargetDetails" in data:
        import capo_supplychain.types.data_integration_event_dataset_target_details

        out["dataset_target_details"] = (
            capo_supplychain.types.data_integration_event_dataset_target_details.deserialize_json(
                data["datasetTargetDetails"]
            )
        )
    return out
