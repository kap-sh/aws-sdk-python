"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InstrumentBalanceToken``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

"""<p>Supported tokens for instrument balance queries. Only tokens supported for X402 payments are returned.</p>"""
InstrumentBalanceToken: TypeAlias = Literal["USDC",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("USDC",))


def serialize_json(value: InstrumentBalanceToken) -> str:
    return value


def deserialize_json(data: str) -> InstrumentBalanceToken:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstrumentBalanceToken value: {data!r}")
    return cast(InstrumentBalanceToken, data)
