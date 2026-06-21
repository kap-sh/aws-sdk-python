"""Generated from Smithy shape ``com.amazonaws.deadline#DependencyConsumerResolutionStatus``."""

from typing import Literal, TypeAlias, cast

DependencyConsumerResolutionStatus: TypeAlias = Literal[
    "RESOLVED",
    "UNRESOLVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DependencyConsumerResolutionStatus) -> str:
    return value


def deserialize_json(data: str) -> DependencyConsumerResolutionStatus:
    return cast(DependencyConsumerResolutionStatus, data)
