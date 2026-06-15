"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Currency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

"""<p>Supported currency codes.</p>"""
Currency: TypeAlias = Literal["USD",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("USD",))


def serialize_json(value: Currency) -> str:
    return value


def deserialize_json(data: str) -> Currency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Currency value: {data!r}")
    return cast(Currency, data)
