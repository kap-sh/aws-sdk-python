"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ConfluenceHostType``."""

from typing import Literal, TypeAlias, cast

ConfluenceHostType: TypeAlias = Literal["SAAS",]


# --- restJson1 ser/de ---
def serialize_json(value: ConfluenceHostType) -> str:
    return value


def deserialize_json(data: str) -> ConfluenceHostType:
    return cast(ConfluenceHostType, data)
