"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfDocumentationVersion``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.documentation_version

ListOfDocumentationVersion: TypeAlias = list[
    "aws_sdk_api_gateway.types.documentation_version.DocumentationVersion"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfDocumentationVersion) -> list:
    import aws_sdk_api_gateway.types.documentation_version

    out: list = []
    for item in value:
        out.append(aws_sdk_api_gateway.types.documentation_version.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfDocumentationVersion:
    import aws_sdk_api_gateway.types.documentation_version

    out: ListOfDocumentationVersion = []
    for item in data:
        out.append(
            aws_sdk_api_gateway.types.documentation_version.deserialize_json(item)
        )
    return out
