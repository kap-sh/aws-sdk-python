"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gameliftstreams.types.arn

ArnList: TypeAlias = list["capo_gameliftstreams.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: ArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ArnList:
    return list(data)
