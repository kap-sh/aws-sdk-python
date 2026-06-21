"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ListTargetsFilterName``."""

from typing import Literal, TypeAlias, cast

ListTargetsFilterName: TypeAlias = Literal[
    "TARGET_TYPE",
    "TARGET_ADDRESS",
    "TARGET_STATUS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ListTargetsFilterName) -> str:
    return value


def deserialize_json(data: str) -> ListTargetsFilterName:
    return cast(ListTargetsFilterName, data)
