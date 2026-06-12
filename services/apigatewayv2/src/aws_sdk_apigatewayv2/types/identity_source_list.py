"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#IdentitySourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string

IdentitySourceList: TypeAlias = list["aws_sdk_apigatewayv2.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: IdentitySourceList) -> list:
    return list(value)


def deserialize_json(data: list) -> IdentitySourceList:
    return list(data)
