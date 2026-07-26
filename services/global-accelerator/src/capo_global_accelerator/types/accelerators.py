"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#Accelerators``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_global_accelerator.types.accelerator

Accelerators: TypeAlias = list["capo_global_accelerator.types.accelerator.Accelerator"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Accelerators) -> list:
    import capo_global_accelerator.types.accelerator

    out: list = []
    for item in value:
        out.append(
            capo_global_accelerator.types.accelerator.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Accelerators:
    import capo_global_accelerator.types.accelerator

    out: Accelerators = []
    for item in data:
        out.append(
            capo_global_accelerator.types.accelerator.deserialize_aws_json_1_1(item)
        )
    return out
