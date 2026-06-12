"""Generated from Smithy shape ``com.amazonaws.apigateway#DocumentationPartIds``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.list_of_string


class DocumentationPartIds(TypedDict):
    ids: NotRequired["aws_sdk_api_gateway.types.list_of_string.ListOfString"]
    """<p>A list of the returned documentation part identifiers.</p>"""
    warnings: NotRequired["aws_sdk_api_gateway.types.list_of_string.ListOfString"]
    """<p>A list of warning messages reported during import of documentation parts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentationPartIds) -> dict:
    out: dict = {}
    if "ids" in value:
        import aws_sdk_api_gateway.types.list_of_string

        out["ids"] = aws_sdk_api_gateway.types.list_of_string.serialize_json(
            value["ids"]
        )
    if "warnings" in value:
        import aws_sdk_api_gateway.types.list_of_string

        out["warnings"] = aws_sdk_api_gateway.types.list_of_string.serialize_json(
            value["warnings"]
        )
    return out


def deserialize_json(data: dict) -> DocumentationPartIds:
    out: DocumentationPartIds = {}  # type: ignore[typeddict-item]
    if "ids" in data:
        import aws_sdk_api_gateway.types.list_of_string

        out["ids"] = aws_sdk_api_gateway.types.list_of_string.deserialize_json(
            data["ids"]
        )
    if "warnings" in data:
        import aws_sdk_api_gateway.types.list_of_string

        out["warnings"] = aws_sdk_api_gateway.types.list_of_string.deserialize_json(
            data["warnings"]
        )
    return out
