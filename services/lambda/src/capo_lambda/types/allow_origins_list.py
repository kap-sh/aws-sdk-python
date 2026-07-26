"""Generated from Smithy shape ``com.amazonaws.lambda#AllowOriginsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.origin

AllowOriginsList: TypeAlias = list["capo_lambda.types.origin.Origin"]


# --- restJson1 ser/de ---
def serialize_json(value: AllowOriginsList) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowOriginsList:
    return list(data)
