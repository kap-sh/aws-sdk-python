"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

"""<p>Transaction status enum.</p>"""
PaymentStatus: TypeAlias = Literal["PROOF_GENERATED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PROOF_GENERATED",))


def serialize_json(value: PaymentStatus) -> str:
    return value


def deserialize_json(data: str) -> PaymentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PaymentStatus value: {data!r}")
    return cast(PaymentStatus, data)
