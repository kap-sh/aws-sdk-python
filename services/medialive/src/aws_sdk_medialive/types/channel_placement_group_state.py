"""Generated from Smithy shape ``com.amazonaws.medialive#ChannelPlacementGroupState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "UNASSIGNED",
        "ASSIGNING",
        "ASSIGNED",
        "DELETING",
        "DELETE_FAILED",
        "DELETED",
        "UNASSIGNING",
    )
)


def serialize_json(value: ChannelPlacementGroupState) -> str:
    return value


def deserialize_json(data: str) -> ChannelPlacementGroupState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ChannelPlacementGroupState value: {data!r}"
        )
    return cast(ChannelPlacementGroupState, data)
