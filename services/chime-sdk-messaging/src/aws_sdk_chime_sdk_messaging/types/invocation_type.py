"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#InvocationType``."""

from typing import Literal, TypeAlias, cast

InvocationType: TypeAlias = Literal["ASYNC",]


# --- restJson1 ser/de ---
def serialize_json(value: InvocationType) -> str:
    return value


def deserialize_json(data: str) -> InvocationType:
    return cast(InvocationType, data)
