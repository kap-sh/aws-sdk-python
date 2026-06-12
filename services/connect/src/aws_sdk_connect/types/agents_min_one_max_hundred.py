"""Generated from Smithy shape ``com.amazonaws.connect#AgentsMinOneMaxHundred``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.user_id

AgentsMinOneMaxHundred: TypeAlias = list["aws_sdk_connect.types.user_id.UserId"]


# --- restJson1 ser/de ---
def serialize_json(value: AgentsMinOneMaxHundred) -> list:
    return list(value)


def deserialize_json(data: list) -> AgentsMinOneMaxHundred:
    return list(data)
