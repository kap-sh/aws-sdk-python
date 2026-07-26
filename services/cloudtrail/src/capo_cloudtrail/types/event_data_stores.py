"""Generated from Smithy shape ``com.amazonaws.cloudtrail#EventDataStores``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.event_data_store

EventDataStores: TypeAlias = list[
    "capo_cloudtrail.types.event_data_store.EventDataStore"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventDataStores) -> list:
    import capo_cloudtrail.types.event_data_store

    out: list = []
    for item in value:
        out.append(capo_cloudtrail.types.event_data_store.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EventDataStores:
    import capo_cloudtrail.types.event_data_store

    out: EventDataStores = []
    for item in data:
        out.append(
            capo_cloudtrail.types.event_data_store.deserialize_aws_json_1_1(item)
        )
    return out
