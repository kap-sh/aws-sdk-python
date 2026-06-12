"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourceGroupByField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

ResourceGroupByField: TypeAlias = Literal[
    "AccountId",
    "Region",
    "ResourceCategory",
    "ResourceType",
    "ResourceName",
    "FindingsSummary.FindingType",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AccountId",
        "Region",
        "ResourceCategory",
        "ResourceType",
        "ResourceName",
        "FindingsSummary.FindingType",
    )
)


def serialize_json(value: ResourceGroupByField) -> str:
    return value


def deserialize_json(data: str) -> ResourceGroupByField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceGroupByField value: {data!r}")
    return cast(ResourceGroupByField, data)
