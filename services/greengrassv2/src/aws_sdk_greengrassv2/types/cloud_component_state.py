"""Generated from Smithy shape ``com.amazonaws.greengrassv2#CloudComponentState``."""

from typing import Literal, TypeAlias, cast

CloudComponentState: TypeAlias = Literal[
    "REQUESTED",
    "INITIATED",
    "DEPLOYABLE",
    "FAILED",
    "DEPRECATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CloudComponentState) -> str:
    return value


def deserialize_json(data: str) -> CloudComponentState:
    return cast(CloudComponentState, data)
