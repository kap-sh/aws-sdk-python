"""Generated from Smithy shape ``com.amazonaws.quicksight#ActionConnectorErrorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ActionConnectorErrorType: TypeAlias = Literal["INTERNAL_FAILURE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("INTERNAL_FAILURE",))


def serialize_json(value: ActionConnectorErrorType) -> str:
    return value


def deserialize_json(data: str) -> ActionConnectorErrorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionConnectorErrorType value: {data!r}")
    return cast(ActionConnectorErrorType, data)
