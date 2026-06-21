"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AttributeMatchingModel``."""

from typing import Literal, TypeAlias, cast

AttributeMatchingModel: TypeAlias = Literal[
    "ONE_TO_ONE",
    "MANY_TO_MANY",
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeMatchingModel) -> str:
    return value


def deserialize_json(data: str) -> AttributeMatchingModel:
    return cast(AttributeMatchingModel, data)
