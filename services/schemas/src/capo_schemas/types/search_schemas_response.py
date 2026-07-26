"""Generated from Smithy shape ``com.amazonaws.schemas#SearchSchemasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_schemas.types.__list_of_search_schema_summary
    import capo_schemas.types.__string


class SearchSchemasResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_schemas.types.__string.__string"]
    """<p>The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.</p>"""
    schemas: NotRequired[
        "capo_schemas.types.__list_of_search_schema_summary.__listOfSearchSchemaSummary"
    ]
    """<p>An array of SearchSchemaSummary information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchSchemasResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "schemas" in value:
        import capo_schemas.types.__list_of_search_schema_summary

        out["Schemas"] = (
            capo_schemas.types.__list_of_search_schema_summary.serialize_json(
                value["schemas"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchSchemasResponse:
    out: SearchSchemasResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Schemas" in data:
        import capo_schemas.types.__list_of_search_schema_summary

        out["schemas"] = (
            capo_schemas.types.__list_of_search_schema_summary.deserialize_json(
                data["Schemas"]
            )
        )
    return out
