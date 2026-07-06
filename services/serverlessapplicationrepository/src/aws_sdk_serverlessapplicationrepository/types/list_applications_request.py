"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#ListApplicationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.__string
    import aws_sdk_serverlessapplicationrepository.types.max_items


class ListApplicationsRequest(TypedDict, closed=True):
    max_items: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.max_items.MaxItems"
    ]
    """<p>The total number of items to return.</p>"""
    next_token: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A token to specify where to start paginating.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListApplicationsRequest:
    out: ListApplicationsRequest = {}  # type: ignore[typeddict-item]
    return out
