"""Generated from Smithy shape ``com.amazonaws.medialive#ChannelPlacementGroupState``."""

from typing import Literal, TypeAlias, cast

"""Used in DescribeChannelPlacementGroupResult"""
ChannelPlacementGroupState: TypeAlias = Literal[
    "UNASSIGNED",
    "ASSIGNING",
    "ASSIGNED",
    "DELETING",
    "DELETE_FAILED",
    "DELETED",
    "UNASSIGNING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelPlacementGroupState) -> str:
    return value


def deserialize_json(data: str) -> ChannelPlacementGroupState:
    return cast(ChannelPlacementGroupState, data)
