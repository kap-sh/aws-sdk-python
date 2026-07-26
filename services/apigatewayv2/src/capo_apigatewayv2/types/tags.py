"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string
    import capo_apigatewayv2.types.string_with_length_between1_and1600

Tags: TypeAlias = dict[
    "capo_apigatewayv2.types.__string.__string",
    "capo_apigatewayv2.types.string_with_length_between1_and1600.StringWithLengthBetween1And1600",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Tags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Tags:
    out: Tags = {}
    for key, value in data.items():
        out[key] = value
    return out
