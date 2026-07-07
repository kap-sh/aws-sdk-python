"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListNotificationChannelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.uuid_next_token


class ListNotificationChannelsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationChannelsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNotificationChannelsRequest:
    out: ListNotificationChannelsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
