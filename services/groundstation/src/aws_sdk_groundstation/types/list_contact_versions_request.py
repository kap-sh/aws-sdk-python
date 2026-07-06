"""Generated from Smithy shape ``com.amazonaws.groundstation#ListContactVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.pagination_max_results
    import aws_sdk_groundstation.types.pagination_token
    import aws_sdk_groundstation.types.uuid


class ListContactVersionsRequest(TypedDict, closed=True):
    contact_id: "aws_sdk_groundstation.types.uuid.Uuid"
    """<p>UUID of a contact.</p>"""
    max_results: NotRequired[
        "aws_sdk_groundstation.types.pagination_max_results.PaginationMaxResults"
    ]
    """<p>Maximum number of contact versions returned.</p>"""
    next_token: NotRequired[
        "aws_sdk_groundstation.types.pagination_token.PaginationToken"
    ]
    """<p>Next token returned in the request of a previous <code>ListContactVersions</code> call. Used to get the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContactVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListContactVersionsRequest:
    out: ListContactVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
