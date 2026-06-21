"""Generated from Smithy shape ``com.amazonaws.mediatailor#Method``."""

from typing import Literal, TypeAlias, cast

Method: TypeAlias = Literal[
    "GET",
    "POST",
]


# --- restJson1 ser/de ---
def serialize_json(value: Method) -> str:
    return value


def deserialize_json(data: str) -> Method:
    return cast(Method, data)
