"""Generated from Smithy shape ``com.amazonaws.personalize#Domain``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_personalize.errors import DeserializationError

Domain: TypeAlias = Literal[
    "ECOMMERCE",
    "VIDEO_ON_DEMAND",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ECOMMERCE",
        "VIDEO_ON_DEMAND",
    )
)


def serialize_aws_json_1_1(value: Domain) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Domain:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Domain value: {data!r}")
    return cast(Domain, data)
