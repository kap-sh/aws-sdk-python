"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ListEventTypesFilterName``."""

from typing import Literal, TypeAlias, cast

ListEventTypesFilterName: TypeAlias = Literal[
    "RESOURCE_TYPE",
    "SERVICE_NAME",
]


# --- restJson1 ser/de ---
def serialize_json(value: ListEventTypesFilterName) -> str:
    return value


def deserialize_json(data: str) -> ListEventTypesFilterName:
    return cast(ListEventTypesFilterName, data)
