"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfARNs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.provider_arn

ListOfARNs: TypeAlias = list["aws_sdk_api_gateway.types.provider_arn.ProviderARN"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfARNs) -> list:
    return list(value)


def deserialize_json(data: list) -> ListOfARNs:
    return list(data)
