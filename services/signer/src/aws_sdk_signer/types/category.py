"""Generated from Smithy shape ``com.amazonaws.signer#Category``."""

from typing import Literal, TypeAlias, cast

Category: TypeAlias = Literal["AWSIoT",]


# --- restJson1 ser/de ---
def serialize_json(value: Category) -> str:
    return value


def deserialize_json(data: str) -> Category:
    return cast(Category, data)
