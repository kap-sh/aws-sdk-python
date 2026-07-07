"""Generated from Smithy shape ``com.amazonaws.apigateway#ApiKeyIds``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.list_of_string


class ApiKeyIds(TypedDict, closed=True):
    ids: NotRequired["aws_sdk_api_gateway.types.list_of_string.ListOfString"]
    """<p>A list of all the ApiKey identifiers.</p>"""
    warnings: NotRequired["aws_sdk_api_gateway.types.list_of_string.ListOfString"]
    """<p>A list of warning messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiKeyIds) -> dict:
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


def deserialize_json(data: dict) -> ApiKeyIds:
    out: ApiKeyIds = {}  # type: ignore[typeddict-item]
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
