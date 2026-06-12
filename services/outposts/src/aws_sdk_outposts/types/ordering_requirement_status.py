"""Generated from Smithy shape ``com.amazonaws.outposts#OrderingRequirementStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

OrderingRequirementStatus: TypeAlias = Literal[
    "PASS",
    "FAIL",
    "EXEMPT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASS",
        "FAIL",
        "EXEMPT",
    )
)


def serialize_json(value: OrderingRequirementStatus) -> str:
    return value


def deserialize_json(data: str) -> OrderingRequirementStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrderingRequirementStatus value: {data!r}")
    return cast(OrderingRequirementStatus, data)
