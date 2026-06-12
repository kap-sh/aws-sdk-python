"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#LinkedServices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.linked_service

LinkedServices: TypeAlias = list[
    "aws_sdk_iottwinmaker.types.linked_service.LinkedService"
]


# --- restJson1 ser/de ---
def serialize_json(value: LinkedServices) -> list:
    return list(value)


def deserialize_json(data: list) -> LinkedServices:
    return list(data)
