"""Generated from Smithy shape ``com.amazonaws.pinpoint#__TimezoneEstimationMethodsElement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

__TimezoneEstimationMethodsElement: TypeAlias = Literal[
    "PHONE_NUMBER",
    "POSTAL_CODE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PHONE_NUMBER",
        "POSTAL_CODE",
    )
)


def serialize_json(value: __TimezoneEstimationMethodsElement) -> str:
    return value


def deserialize_json(data: str) -> __TimezoneEstimationMethodsElement:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown __TimezoneEstimationMethodsElement value: {data!r}"
        )
    return cast(__TimezoneEstimationMethodsElement, data)
