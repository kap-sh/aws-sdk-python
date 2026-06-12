"""Generated from Smithy shape ``com.amazonaws.mq#PromoteMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mq.errors import DeserializationError

"""<p>The Promote mode requested.</p>"""
PromoteMode: TypeAlias = Literal[
    "SWITCHOVER",
    "FAILOVER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SWITCHOVER",
        "FAILOVER",
    )
)


def serialize_json(value: PromoteMode) -> str:
    return value


def deserialize_json(data: str) -> PromoteMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PromoteMode value: {data!r}")
    return cast(PromoteMode, data)
