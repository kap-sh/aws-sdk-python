"""Generated from Smithy shape ``com.amazonaws.rtbfabric#RuleStatus``."""

from typing import Literal, TypeAlias, cast

"""Status of a routing rule"""
RuleStatus: TypeAlias = Literal[
    "CREATION_IN_PROGRESS",
    "ACTIVE",
    "UPDATE_IN_PROGRESS",
    "DELETION_IN_PROGRESS",
    "DELETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleStatus) -> str:
    return value


def deserialize_json(data: str) -> RuleStatus:
    return cast(RuleStatus, data)
