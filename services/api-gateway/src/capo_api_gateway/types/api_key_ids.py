"""Generated from Smithy shape ``com.amazonaws.apigateway#ApiKeyIds``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_string


class ApiKeyIds(TypedDict, closed=True):
    ids: NotRequired["capo_api_gateway.types.list_of_string.ListOfString"]
    """<p>A list of all the ApiKey identifiers.</p>"""
    warnings: NotRequired["capo_api_gateway.types.list_of_string.ListOfString"]
    """<p>A list of warning messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiKeyIds) -> dict:
    out: dict = {}
    if "ids" in value:
        import capo_api_gateway.types.list_of_string

        out["ids"] = capo_api_gateway.types.list_of_string.serialize_json(value["ids"])
    if "warnings" in value:
        import capo_api_gateway.types.list_of_string

        out["warnings"] = capo_api_gateway.types.list_of_string.serialize_json(
            value["warnings"]
        )
    return out


def deserialize_json(data: dict) -> ApiKeyIds:
    out: ApiKeyIds = {}  # type: ignore[typeddict-item]
    if "ids" in data:
        import capo_api_gateway.types.list_of_string

        out["ids"] = capo_api_gateway.types.list_of_string.deserialize_json(data["ids"])
    if "warnings" in data:
        import capo_api_gateway.types.list_of_string

        out["warnings"] = capo_api_gateway.types.list_of_string.deserialize_json(
            data["warnings"]
        )
    return out
