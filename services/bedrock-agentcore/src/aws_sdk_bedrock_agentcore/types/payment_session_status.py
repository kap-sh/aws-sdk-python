"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentSessionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

"""<p>The status of a payment session.</p>"""
PaymentSessionStatus: TypeAlias = Literal[
    "ACTIVE",
    "EXPIRED",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "EXPIRED",
        "DELETED",
    )
)


def serialize_json(value: PaymentSessionStatus) -> str:
    return value


def deserialize_json(data: str) -> PaymentSessionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PaymentSessionStatus value: {data!r}")
    return cast(PaymentSessionStatus, data)
