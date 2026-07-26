"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#AcceleratorEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_global_accelerator.types.accelerator_event

AcceleratorEvents: TypeAlias = list[
    "capo_global_accelerator.types.accelerator_event.AcceleratorEvent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceleratorEvents) -> list:
    import capo_global_accelerator.types.accelerator_event

    out: list = []
    for item in value:
        out.append(
            capo_global_accelerator.types.accelerator_event.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AcceleratorEvents:
    import capo_global_accelerator.types.accelerator_event

    out: AcceleratorEvents = []
    for item in data:
        out.append(
            capo_global_accelerator.types.accelerator_event.deserialize_aws_json_1_1(
                item
            )
        )
    return out
