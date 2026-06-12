"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourcesGroupingRecGenStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

ResourcesGroupingRecGenStatusType: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Failed",
    "Success",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "InProgress",
        "Failed",
        "Success",
    )
)


def serialize_json(value: ResourcesGroupingRecGenStatusType) -> str:
    return value


def deserialize_json(data: str) -> ResourcesGroupingRecGenStatusType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResourcesGroupingRecGenStatusType value: {data!r}"
        )
    return cast(ResourcesGroupingRecGenStatusType, data)
