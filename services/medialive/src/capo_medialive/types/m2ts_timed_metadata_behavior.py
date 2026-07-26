"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsTimedMetadataBehavior``."""

from typing import Literal, TypeAlias, cast

"""M2ts Timed Metadata Behavior"""
M2tsTimedMetadataBehavior: TypeAlias = Literal[
    "NO_PASSTHROUGH",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsTimedMetadataBehavior) -> str:
    return value


def deserialize_json(data: str) -> M2tsTimedMetadataBehavior:
    return cast(M2tsTimedMetadataBehavior, data)
