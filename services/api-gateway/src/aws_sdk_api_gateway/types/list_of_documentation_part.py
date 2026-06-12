"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfDocumentationPart``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.documentation_part

ListOfDocumentationPart: TypeAlias = list[
    "aws_sdk_api_gateway.types.documentation_part.DocumentationPart"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfDocumentationPart) -> list:
    import aws_sdk_api_gateway.types.documentation_part

    out: list = []
    for item in value:
        out.append(aws_sdk_api_gateway.types.documentation_part.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfDocumentationPart:
    import aws_sdk_api_gateway.types.documentation_part

    out: ListOfDocumentationPart = []
    for item in data:
        out.append(aws_sdk_api_gateway.types.documentation_part.deserialize_json(item))
    return out
