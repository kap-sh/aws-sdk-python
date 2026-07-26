"""Generated from Smithy shape ``com.amazonaws.controlcatalog#CommonControlArnFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controlcatalog.types.common_control_arn

CommonControlArnFilterList: TypeAlias = list[
    "capo_controlcatalog.types.common_control_arn.CommonControlArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: CommonControlArnFilterList) -> list:
    return list(value)


def deserialize_json(data: list) -> CommonControlArnFilterList:
    return list(data)
