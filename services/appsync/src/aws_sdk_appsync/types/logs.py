"""Generated from Smithy shape ``com.amazonaws.appsync#Logs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appsync.types.string

Logs: TypeAlias = list["aws_sdk_appsync.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: Logs) -> list:
    return list(value)


def deserialize_json(data: list) -> Logs:
    return list(data)
