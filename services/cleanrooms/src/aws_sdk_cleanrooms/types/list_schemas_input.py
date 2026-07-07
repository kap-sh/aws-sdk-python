"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListSchemasInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_identifier
    import aws_sdk_cleanrooms.types.max_results
    import aws_sdk_cleanrooms.types.pagination_token
    import aws_sdk_cleanrooms.types.schema_type


class ListSchemasInput(TypedDict, closed=True):
    collaboration_identifier: (
        "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID.</p>"""
    schema_type: NotRequired["aws_sdk_cleanrooms.types.schema_type.SchemaType"]
    """<p>If present, filter schemas by schema type.</p>"""
    next_token: NotRequired["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_cleanrooms.types.max_results.MaxResults"]
    """<p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSchemasInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSchemasInput:
    out: ListSchemasInput = {}  # type: ignore[typeddict-item]
    return out
