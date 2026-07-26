"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InstrumentBalanceToken``."""

from typing import Literal, TypeAlias, cast

"""<p>Supported tokens for instrument balance queries. Only tokens supported for X402 payments are returned.</p>"""
InstrumentBalanceToken: TypeAlias = Literal["USDC",]


# --- restJson1 ser/de ---
def serialize_json(value: InstrumentBalanceToken) -> str:
    return value


def deserialize_json(data: str) -> InstrumentBalanceToken:
    return cast(InstrumentBalanceToken, data)
