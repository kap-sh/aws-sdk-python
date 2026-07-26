"""Generated from Smithy shape ``com.amazonaws.quicksight#LinkEntityArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.link_entity_arn

LinkEntityArnList: TypeAlias = list[
    "capo_quicksight.types.link_entity_arn.LinkEntityArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: LinkEntityArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> LinkEntityArnList:
    return list(data)
