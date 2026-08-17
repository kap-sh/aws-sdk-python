"""Generated from Smithy shape ``com.amazonaws.lambda#HeadersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.header

HeadersList: TypeAlias = list["capo_lambda.types.header.Header"]


# --- restJson1 ser/de ---
def serialize_json(value: HeadersList) -> list:
    return list(value)


def deserialize_json(data: list) -> HeadersList:
    return [item for item in data if item is not None]
