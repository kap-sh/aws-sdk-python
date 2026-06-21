"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InputQueryType``."""

from typing import Literal, TypeAlias, cast

InputQueryType: TypeAlias = Literal["TEXT",]


# --- restJson1 ser/de ---
def serialize_json(value: InputQueryType) -> str:
    return value


def deserialize_json(data: str) -> InputQueryType:
    return cast(InputQueryType, data)
