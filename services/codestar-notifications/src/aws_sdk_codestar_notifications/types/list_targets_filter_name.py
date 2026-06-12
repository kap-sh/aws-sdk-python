"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ListTargetsFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codestar_notifications.errors import DeserializationError

ListTargetsFilterName: TypeAlias = Literal[
    "TARGET_TYPE",
    "TARGET_ADDRESS",
    "TARGET_STATUS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TARGET_TYPE",
        "TARGET_ADDRESS",
        "TARGET_STATUS",
    )
)


def serialize_json(value: ListTargetsFilterName) -> str:
    return value


def deserialize_json(data: str) -> ListTargetsFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListTargetsFilterName value: {data!r}")
    return cast(ListTargetsFilterName, data)
