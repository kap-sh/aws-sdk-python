"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IncompatibleLoopNodeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

IncompatibleLoopNodeType: TypeAlias = Literal[
    "Input",
    "Condition",
    "Iterator",
    "Collector",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Input",
        "Condition",
        "Iterator",
        "Collector",
    )
)


def serialize_json(value: IncompatibleLoopNodeType) -> str:
    return value


def deserialize_json(data: str) -> IncompatibleLoopNodeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IncompatibleLoopNodeType value: {data!r}")
    return cast(IncompatibleLoopNodeType, data)
