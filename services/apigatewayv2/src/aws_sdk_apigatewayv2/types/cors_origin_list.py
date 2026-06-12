"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#CorsOriginList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string

CorsOriginList: TypeAlias = list["aws_sdk_apigatewayv2.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: CorsOriginList) -> list:
    return list(value)


def deserialize_json(data: list) -> CorsOriginList:
    return list(data)
