"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#CorsHeaderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string

CorsHeaderList: TypeAlias = list["capo_apigatewayv2.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: CorsHeaderList) -> list:
    return list(value)


def deserialize_json(data: list) -> CorsHeaderList:
    return list(data)
