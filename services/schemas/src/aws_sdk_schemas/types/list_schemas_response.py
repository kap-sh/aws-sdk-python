"""Generated from Smithy shape ``com.amazonaws.schemas#ListSchemasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__list_of_schema_summary
    import aws_sdk_schemas.types.__string


class ListSchemasResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.</p>"""
    schemas: NotRequired[
        "aws_sdk_schemas.types.__list_of_schema_summary.__listOfSchemaSummary"
    ]
    """<p>An array of schema summaries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSchemasResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "schemas" in value:
        import aws_sdk_schemas.types.__list_of_schema_summary

        out["Schemas"] = aws_sdk_schemas.types.__list_of_schema_summary.serialize_json(
            value["schemas"]
        )
    return out


def deserialize_json(data: dict) -> ListSchemasResponse:
    out: ListSchemasResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Schemas" in data:
        import aws_sdk_schemas.types.__list_of_schema_summary

        out["schemas"] = (
            aws_sdk_schemas.types.__list_of_schema_summary.deserialize_json(
                data["Schemas"]
            )
        )
    return out
