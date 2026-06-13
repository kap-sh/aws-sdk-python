"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#PolicyComponent``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

PolicyComponent: TypeAlias = Literal[
    "AVAILABILITY_SLO",
    "MULTI_AZ_DISASTER_RECOVERY",
    "MULTI_REGION_DISASTER_RECOVERY",
    "DATA_RECOVERY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABILITY_SLO",
        "MULTI_AZ_DISASTER_RECOVERY",
        "MULTI_REGION_DISASTER_RECOVERY",
        "DATA_RECOVERY",
    )
)


def serialize_json(value: PolicyComponent) -> str:
    return value


def deserialize_json(data: str) -> PolicyComponent:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PolicyComponent value: {data!r}")
    return cast(PolicyComponent, data)
