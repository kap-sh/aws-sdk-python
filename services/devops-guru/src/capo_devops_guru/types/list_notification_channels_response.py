"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListNotificationChannelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.channels
    import capo_devops_guru.types.uuid_next_token


class ListNotificationChannelsResponse(TypedDict, closed=True):
    channels: NotRequired["capo_devops_guru.types.channels.Channels"]
    """<p> An array that contains the requested notification channels. </p>"""
    next_token: NotRequired["capo_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationChannelsResponse) -> dict:
    out: dict = {}
    if "channels" in value:
        import capo_devops_guru.types.channels

        out["Channels"] = capo_devops_guru.types.channels.serialize_json(
            value["channels"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNotificationChannelsResponse:
    out: ListNotificationChannelsResponse = {}  # type: ignore[typeddict-item]
    if "Channels" in data:
        import capo_devops_guru.types.channels

        out["channels"] = capo_devops_guru.types.channels.deserialize_json(
            data["Channels"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
