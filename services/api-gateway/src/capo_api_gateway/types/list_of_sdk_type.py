"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfSdkType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.sdk_type

ListOfSdkType: TypeAlias = list["capo_api_gateway.types.sdk_type.SdkType"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfSdkType) -> list:
    import capo_api_gateway.types.sdk_type

    out: list = []
    for item in value:
        out.append(capo_api_gateway.types.sdk_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfSdkType:
    import capo_api_gateway.types.sdk_type

    out: ListOfSdkType = []
    for item in data:
        out.append(capo_api_gateway.types.sdk_type.deserialize_json(item))
    return out
