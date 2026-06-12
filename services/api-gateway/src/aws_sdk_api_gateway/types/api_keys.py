"""Generated from Smithy shape ``com.amazonaws.apigateway#ApiKeys``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.list_of_api_key
    import aws_sdk_api_gateway.types.list_of_string
    import aws_sdk_api_gateway.types.string


class ApiKeys(TypedDict):
    warnings: NotRequired["aws_sdk_api_gateway.types.list_of_string.ListOfString"]
    """<p>A list of warning messages logged during the import of API keys when the <code>failOnWarnings</code> option is set to true.</p>"""
    items: NotRequired["aws_sdk_api_gateway.types.list_of_api_key.ListOfApiKey"]
    """<p>The current page of elements from this collection.</p>"""
    position: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiKeys) -> dict:
    out: dict = {}
    if "warnings" in value:
        import aws_sdk_api_gateway.types.list_of_string

        out["warnings"] = aws_sdk_api_gateway.types.list_of_string.serialize_json(
            value["warnings"]
        )
    if "items" in value:
        import aws_sdk_api_gateway.types.list_of_api_key

        out["item"] = aws_sdk_api_gateway.types.list_of_api_key.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> ApiKeys:
    out: ApiKeys = {}  # type: ignore[typeddict-item]
    if "warnings" in data:
        import aws_sdk_api_gateway.types.list_of_string

        out["warnings"] = aws_sdk_api_gateway.types.list_of_string.deserialize_json(
            data["warnings"]
        )
    if "item" in data:
        import aws_sdk_api_gateway.types.list_of_api_key

        out["items"] = aws_sdk_api_gateway.types.list_of_api_key.deserialize_json(
            data["item"]
        )
    return out
