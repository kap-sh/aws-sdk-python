"""Generated from Smithy shape ``com.amazonaws.resiliencehub#String255List``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.string255

String255List: TypeAlias = list["aws_sdk_resiliencehub.types.string255.String255"]


# --- restJson1 ser/de ---
def serialize_json(value: String255List) -> list:
    return list(value)


def deserialize_json(data: list) -> String255List:
    return list(data)
