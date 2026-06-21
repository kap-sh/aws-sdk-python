"""Generated from Smithy shape ``com.amazonaws.appconfig#BadRequestReason``."""

from typing import Literal, TypeAlias, cast

BadRequestReason: TypeAlias = Literal["InvalidConfiguration",]


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestReason) -> str:
    return value


def deserialize_json(data: str) -> BadRequestReason:
    return cast(BadRequestReason, data)
