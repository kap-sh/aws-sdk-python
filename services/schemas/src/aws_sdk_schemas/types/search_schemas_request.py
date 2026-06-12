"""Generated from Smithy shape ``com.amazonaws.schemas#SearchSchemasRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__integer
    import aws_sdk_schemas.types.__string


class SearchSchemasRequest(TypedDict):
    keywords: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>Specifying this limits the results to only schemas that include the provided keywords.</p>"""
    limit: NotRequired["aws_sdk_schemas.types.__integer.__integer"]
    next_token: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.</p>"""
    registry_name: "aws_sdk_schemas.types.__string.__string"
    """<p>The name of the registry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchSchemasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SearchSchemasRequest:
    out: SearchSchemasRequest = {}  # type: ignore[typeddict-item]
    return out
