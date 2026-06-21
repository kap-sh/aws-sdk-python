"""Generated from Smithy shape ``com.amazonaws.mediatailor#Operator``."""

from typing import Literal, TypeAlias, cast

Operator: TypeAlias = Literal["EQUALS",]


# --- restJson1 ser/de ---
def serialize_json(value: Operator) -> str:
    return value


def deserialize_json(data: str) -> Operator:
    return cast(Operator, data)
