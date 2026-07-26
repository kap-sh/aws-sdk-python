"""Generated from Smithy shape ``com.amazonaws.inspector2#FilterArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.filter_arn

FilterArnList: TypeAlias = list["capo_inspector2.types.filter_arn.FilterArn"]


# --- restJson1 ser/de ---
def serialize_json(value: FilterArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> FilterArnList:
    return list(data)
