"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobType``."""

from typing import Literal, TypeAlias, cast

ProtectedJobType: TypeAlias = Literal["PYSPARK",]


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobType) -> str:
    return value


def deserialize_json(data: str) -> ProtectedJobType:
    return cast(ProtectedJobType, data)
