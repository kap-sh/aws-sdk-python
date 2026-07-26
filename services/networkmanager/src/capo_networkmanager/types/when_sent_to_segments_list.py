"""Generated from Smithy shape ``com.amazonaws.networkmanager#WhenSentToSegmentsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string

WhenSentToSegmentsList: TypeAlias = list[
    "capo_networkmanager.types.constrained_string.ConstrainedString"
]


# --- restJson1 ser/de ---
def serialize_json(value: WhenSentToSegmentsList) -> list:
    return list(value)


def deserialize_json(data: list) -> WhenSentToSegmentsList:
    return list(data)
