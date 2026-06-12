"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AttributeMatchingModel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

AttributeMatchingModel: TypeAlias = Literal[
    "ONE_TO_ONE",
    "MANY_TO_MANY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONE_TO_ONE",
        "MANY_TO_MANY",
    )
)


def serialize_json(value: AttributeMatchingModel) -> str:
    return value


def deserialize_json(data: str) -> AttributeMatchingModel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttributeMatchingModel value: {data!r}")
    return cast(AttributeMatchingModel, data)
