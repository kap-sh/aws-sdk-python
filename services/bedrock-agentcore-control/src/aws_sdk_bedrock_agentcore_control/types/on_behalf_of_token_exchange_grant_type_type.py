"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#OnBehalfOfTokenExchangeGrantTypeType``."""

from typing import Literal, TypeAlias, cast

OnBehalfOfTokenExchangeGrantTypeType: TypeAlias = Literal[
    "TOKEN_EXCHANGE",
    "JWT_AUTHORIZATION_GRANT",
]


# --- restJson1 ser/de ---
def serialize_json(value: OnBehalfOfTokenExchangeGrantTypeType) -> str:
    return value


def deserialize_json(data: str) -> OnBehalfOfTokenExchangeGrantTypeType:
    return cast(OnBehalfOfTokenExchangeGrantTypeType, data)
