"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#Names``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.name

Names: TypeAlias = list["aws_sdk_codeguru_reviewer.types.name.Name"]


# --- restJson1 ser/de ---
def serialize_json(value: Names) -> list:
    return list(value)


def deserialize_json(data: list) -> Names:
    return list(data)
