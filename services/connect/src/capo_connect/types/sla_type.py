"""Generated from Smithy shape ``com.amazonaws.connect#SlaType``."""

from typing import Literal, TypeAlias, cast

SlaType: TypeAlias = Literal["CaseField",]


# --- restJson1 ser/de ---
def serialize_json(value: SlaType) -> str:
    return value


def deserialize_json(data: str) -> SlaType:
    return cast(SlaType, data)
