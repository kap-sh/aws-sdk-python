"""Generated from Smithy shape ``com.amazonaws.schemas#ListDiscoverersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__integer
    import aws_sdk_schemas.types.__string


class ListDiscoverersRequest(TypedDict):
    discoverer_id_prefix: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>Specifying this limits the results to only those discoverer IDs that start with the specified prefix.</p>"""
    limit: NotRequired["aws_sdk_schemas.types.__integer.__integer"]
    next_token: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.</p>"""
    source_arn_prefix: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>Specifying this limits the results to only those ARNs that start with the specified prefix.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDiscoverersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDiscoverersRequest:
    out: ListDiscoverersRequest = {}  # type: ignore[typeddict-item]
    return out
