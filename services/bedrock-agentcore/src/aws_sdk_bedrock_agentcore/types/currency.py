"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Currency``."""

from typing import Literal, TypeAlias, cast

"""<p>Supported currency codes.</p>"""
Currency: TypeAlias = Literal["USD",]


# --- restJson1 ser/de ---
def serialize_json(value: Currency) -> str:
    return value


def deserialize_json(data: str) -> Currency:
    return cast(Currency, data)
