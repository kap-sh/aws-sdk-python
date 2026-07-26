"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ListGroupingStatusesFilterName``."""

from typing import Literal, TypeAlias, cast

ListGroupingStatusesFilterName: TypeAlias = Literal[
    "status",
    "resource-arn",
]


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupingStatusesFilterName) -> str:
    return value


def deserialize_json(data: str) -> ListGroupingStatusesFilterName:
    return cast(ListGroupingStatusesFilterName, data)
