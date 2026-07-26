"""Generated from Smithy shape ``com.amazonaws.wickr#BatchDeviceSuccessResponseItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wickr.types.batch_device_success_response_item

BatchDeviceSuccessResponseItems: TypeAlias = list[
    "capo_wickr.types.batch_device_success_response_item.BatchDeviceSuccessResponseItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeviceSuccessResponseItems) -> list:
    import capo_wickr.types.batch_device_success_response_item

    out: list = []
    for item in value:
        out.append(
            capo_wickr.types.batch_device_success_response_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchDeviceSuccessResponseItems:
    import capo_wickr.types.batch_device_success_response_item

    out: BatchDeviceSuccessResponseItems = []
    for item in data:
        out.append(
            capo_wickr.types.batch_device_success_response_item.deserialize_json(item)
        )
    return out
