"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ResponderErrorMaskingAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rtbfabric.errors import DeserializationError

ResponderErrorMaskingAction: TypeAlias = Literal[
    "NO_BID",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_BID",
        "PASSTHROUGH",
    )
)


def serialize_json(value: ResponderErrorMaskingAction) -> str:
    return value


def deserialize_json(data: str) -> ResponderErrorMaskingAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResponderErrorMaskingAction value: {data!r}"
        )
    return cast(ResponderErrorMaskingAction, data)
