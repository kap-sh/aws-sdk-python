"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#TemplateMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string
    import capo_apigatewayv2.types.string_with_length_between0_and32_k

TemplateMap: TypeAlias = dict[
    "capo_apigatewayv2.types.__string.__string",
    "capo_apigatewayv2.types.string_with_length_between0_and32_k.StringWithLengthBetween0And32K",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TemplateMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> TemplateMap:
    out: TemplateMap = {}
    for key, value in data.items():
        out[key] = value
    return out
