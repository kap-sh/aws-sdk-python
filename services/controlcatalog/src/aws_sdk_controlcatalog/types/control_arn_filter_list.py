"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ControlArnFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.control_arn

ControlArnFilterList: TypeAlias = list[
    "aws_sdk_controlcatalog.types.control_arn.ControlArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlArnFilterList) -> list:
    return list(value)


def deserialize_json(data: list) -> ControlArnFilterList:
    return list(data)
