"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#ListApplicationVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.__string
    import aws_sdk_serverlessapplicationrepository.types.max_items


class ListApplicationVersionsRequest(TypedDict):
    application_id: "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    max_items: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.max_items.MaxItems"
    ]
    """<p>The total number of items to return.</p>"""
    next_token: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A token to specify where to start paginating.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListApplicationVersionsRequest:
    out: ListApplicationVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
