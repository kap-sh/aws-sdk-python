"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#SubnetIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string

SubnetIdList: TypeAlias = list["capo_apigatewayv2.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: SubnetIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> SubnetIdList:
    return list(data)
