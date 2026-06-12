"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ListGroupingStatusesFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resource_groups.errors import DeserializationError

ListGroupingStatusesFilterName: TypeAlias = Literal[
    "status",
    "resource-arn",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "status",
        "resource-arn",
    )
)


def serialize_json(value: ListGroupingStatusesFilterName) -> str:
    return value


def deserialize_json(data: str) -> ListGroupingStatusesFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ListGroupingStatusesFilterName value: {data!r}"
        )
    return cast(ListGroupingStatusesFilterName, data)
