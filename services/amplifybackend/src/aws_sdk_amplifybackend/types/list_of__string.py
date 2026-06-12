"""Generated from Smithy shape ``com.amazonaws.amplifybackend#ListOf__string``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string

ListOf__string: TypeAlias = list["aws_sdk_amplifybackend.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOf__string) -> list:
    return list(value)


def deserialize_json(data: list) -> ListOf__string:
    return list(data)
