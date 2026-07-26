"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfTransferringInputDeviceSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.transferring_input_device_summary

__listOfTransferringInputDeviceSummary: TypeAlias = list[
    "capo_medialive.types.transferring_input_device_summary.TransferringInputDeviceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfTransferringInputDeviceSummary) -> list:
    import capo_medialive.types.transferring_input_device_summary

    out: list = []
    for item in value:
        out.append(
            capo_medialive.types.transferring_input_device_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfTransferringInputDeviceSummary:
    import capo_medialive.types.transferring_input_device_summary

    out: __listOfTransferringInputDeviceSummary = []
    for item in data:
        out.append(
            capo_medialive.types.transferring_input_device_summary.deserialize_json(
                item
            )
        )
    return out
