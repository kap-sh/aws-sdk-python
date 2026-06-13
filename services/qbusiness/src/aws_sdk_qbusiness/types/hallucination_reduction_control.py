"""Generated from Smithy shape ``com.amazonaws.qbusiness#HallucinationReductionControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

HallucinationReductionControl: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: HallucinationReductionControl) -> str:
    return value


def deserialize_json(data: str) -> HallucinationReductionControl:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown HallucinationReductionControl value: {data!r}"
        )
    return cast(HallucinationReductionControl, data)
