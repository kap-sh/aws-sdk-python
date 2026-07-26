"""Generated from Smithy shape ``com.amazonaws.finspacedata#locationType``."""

from typing import Literal, TypeAlias, cast

locationType: TypeAlias = Literal[
    "INGESTION",
    "SAGEMAKER",
]


# --- restJson1 ser/de ---
def serialize_json(value: locationType) -> str:
    return value


def deserialize_json(data: str) -> locationType:
    return cast(locationType, data)
