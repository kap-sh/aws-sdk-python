"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfRequestValidator``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.request_validator

ListOfRequestValidator: TypeAlias = list[
    "aws_sdk_api_gateway.types.request_validator.RequestValidator"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfRequestValidator) -> list:
    import aws_sdk_api_gateway.types.request_validator

    out: list = []
    for item in value:
        out.append(aws_sdk_api_gateway.types.request_validator.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfRequestValidator:
    import aws_sdk_api_gateway.types.request_validator

    out: ListOfRequestValidator = []
    for item in data:
        out.append(aws_sdk_api_gateway.types.request_validator.deserialize_json(item))
    return out
