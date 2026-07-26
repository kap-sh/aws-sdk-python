"""Generated from Smithy shape ``com.amazonaws.rbin#ResourceNotFoundExceptionReason``."""

from typing import Literal, TypeAlias, cast

ResourceNotFoundExceptionReason: TypeAlias = Literal["RULE_NOT_FOUND",]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ResourceNotFoundExceptionReason:
    return cast(ResourceNotFoundExceptionReason, data)
