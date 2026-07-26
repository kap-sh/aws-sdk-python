"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#SecurityGroupIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string

SecurityGroupIdList: TypeAlias = list["capo_apigatewayv2.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> SecurityGroupIdList:
    return list(data)
