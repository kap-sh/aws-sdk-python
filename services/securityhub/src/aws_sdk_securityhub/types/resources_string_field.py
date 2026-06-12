"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesStringField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

ResourcesStringField: TypeAlias = Literal[
    "ResourceGuid",
    "ResourceId",
    "AccountId",
    "Region",
    "ResourceCategory",
    "ResourceType",
    "ResourceName",
    "FindingsSummary.FindingType",
    "FindingsSummary.ProductName",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ResourceGuid",
        "ResourceId",
        "AccountId",
        "Region",
        "ResourceCategory",
        "ResourceType",
        "ResourceName",
        "FindingsSummary.FindingType",
        "FindingsSummary.ProductName",
    )
)


def serialize_json(value: ResourcesStringField) -> str:
    return value


def deserialize_json(data: str) -> ResourcesStringField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourcesStringField value: {data!r}")
    return cast(ResourcesStringField, data)
