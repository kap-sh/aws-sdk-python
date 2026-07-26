"""Generated from Smithy shape ``com.amazonaws.iotdataplane#SubscriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_data_plane.types.subscription_summary

SubscriptionList: TypeAlias = list[
    "capo_iot_data_plane.types.subscription_summary.SubscriptionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionList) -> list:
    import capo_iot_data_plane.types.subscription_summary

    out: list = []
    for item in value:
        out.append(capo_iot_data_plane.types.subscription_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SubscriptionList:
    import capo_iot_data_plane.types.subscription_summary

    out: SubscriptionList = []
    for item in data:
        out.append(
            capo_iot_data_plane.types.subscription_summary.deserialize_json(item)
        )
    return out
