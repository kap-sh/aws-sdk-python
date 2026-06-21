"""Generated from Smithy shape ``com.amazonaws.securityhub#SecurityControlProperty``."""

from typing import Literal, TypeAlias, cast

SecurityControlProperty: TypeAlias = Literal["Parameters",]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityControlProperty) -> str:
    return value


def deserialize_json(data: str) -> SecurityControlProperty:
    return cast(SecurityControlProperty, data)
