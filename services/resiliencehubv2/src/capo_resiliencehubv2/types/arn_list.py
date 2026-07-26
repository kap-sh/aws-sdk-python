"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn

ArnList: TypeAlias = list["capo_resiliencehubv2.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: ArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ArnList:
    return list(data)
