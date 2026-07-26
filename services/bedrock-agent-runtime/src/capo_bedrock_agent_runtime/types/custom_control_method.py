"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#CustomControlMethod``."""

from typing import Literal, TypeAlias, cast

CustomControlMethod: TypeAlias = Literal["RETURN_CONTROL",]


# --- restJson1 ser/de ---
def serialize_json(value: CustomControlMethod) -> str:
    return value


def deserialize_json(data: str) -> CustomControlMethod:
    return cast(CustomControlMethod, data)
