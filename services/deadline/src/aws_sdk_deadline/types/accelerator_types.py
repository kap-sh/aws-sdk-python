"""Generated from Smithy shape ``com.amazonaws.deadline#AcceleratorTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.accelerator_type

AcceleratorTypes: TypeAlias = list[
    "aws_sdk_deadline.types.accelerator_type.AcceleratorType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AcceleratorTypes) -> list:
    import aws_sdk_deadline.types.accelerator_type

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.accelerator_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> AcceleratorTypes:
    import aws_sdk_deadline.types.accelerator_type

    out: AcceleratorTypes = []
    for item in data:
        out.append(aws_sdk_deadline.types.accelerator_type.deserialize_json(item))
    return out
