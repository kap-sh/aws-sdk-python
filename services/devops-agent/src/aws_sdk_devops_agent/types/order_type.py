"""Generated from Smithy shape ``com.amazonaws.devopsagent#OrderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>Sort order options for journal operations</p>"""
OrderType: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASC",
        "DESC",
    )
)


def serialize_json(value: OrderType) -> str:
    return value


def deserialize_json(data: str) -> OrderType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrderType value: {data!r}")
    return cast(OrderType, data)
