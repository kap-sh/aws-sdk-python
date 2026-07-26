"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#CorsMethodList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.string_with_length_between1_and64

CorsMethodList: TypeAlias = list[
    "capo_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
]


# --- restJson1 ser/de ---
def serialize_json(value: CorsMethodList) -> list:
    return list(value)


def deserialize_json(data: list) -> CorsMethodList:
    return list(data)
