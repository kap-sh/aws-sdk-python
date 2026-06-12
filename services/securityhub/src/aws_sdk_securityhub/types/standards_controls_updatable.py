"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsControlsUpdatable``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

StandardsControlsUpdatable: TypeAlias = Literal[
    "READY_FOR_UPDATES",
    "NOT_READY_FOR_UPDATES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READY_FOR_UPDATES",
        "NOT_READY_FOR_UPDATES",
    )
)


def serialize_json(value: StandardsControlsUpdatable) -> str:
    return value


def deserialize_json(data: str) -> StandardsControlsUpdatable:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown StandardsControlsUpdatable value: {data!r}"
        )
    return cast(StandardsControlsUpdatable, data)
