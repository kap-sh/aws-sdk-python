"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOf__stringMin20Max2048``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string_min20_max2048

__listOf__stringMin20Max2048: TypeAlias = list[
    "capo_apigatewayv2.types.__string_min20_max2048.__stringMin20Max2048"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOf__stringMin20Max2048) -> list:
    return list(value)


def deserialize_json(data: list) -> __listOf__stringMin20Max2048:
    return list(data)
