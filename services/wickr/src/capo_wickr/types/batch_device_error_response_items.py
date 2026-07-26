"""Generated from Smithy shape ``com.amazonaws.wickr#BatchDeviceErrorResponseItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wickr.types.batch_device_error_response_item

BatchDeviceErrorResponseItems: TypeAlias = list[
    "capo_wickr.types.batch_device_error_response_item.BatchDeviceErrorResponseItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeviceErrorResponseItems) -> list:
    import capo_wickr.types.batch_device_error_response_item

    out: list = []
    for item in value:
        out.append(
            capo_wickr.types.batch_device_error_response_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchDeviceErrorResponseItems:
    import capo_wickr.types.batch_device_error_response_item

    out: BatchDeviceErrorResponseItems = []
    for item in data:
        out.append(
            capo_wickr.types.batch_device_error_response_item.deserialize_json(item)
        )
    return out
