"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#LanguageCode``."""

from typing import Literal, TypeAlias, cast

LanguageCode: TypeAlias = Literal["en-US",]


# --- restJson1 ser/de ---
def serialize_json(value: LanguageCode) -> str:
    return value


def deserialize_json(data: str) -> LanguageCode:
    return cast(LanguageCode, data)
