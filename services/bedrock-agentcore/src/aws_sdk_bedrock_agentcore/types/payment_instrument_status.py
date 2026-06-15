"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentInstrumentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

"""<p>The status of a payment instrument.</p>"""
PaymentInstrumentStatus: TypeAlias = Literal[
    "INITIATED",
    "ACTIVE",
    "FAILED",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIATED",
        "ACTIVE",
        "FAILED",
        "DELETED",
    )
)


def serialize_json(value: PaymentInstrumentStatus) -> str:
    return value


def deserialize_json(data: str) -> PaymentInstrumentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PaymentInstrumentStatus value: {data!r}")
    return cast(PaymentInstrumentStatus, data)
