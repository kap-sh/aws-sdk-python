"""Generated from Smithy shape ``com.amazonaws.medialive#ListChannelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of_channel_summary
    import capo_medialive.types.__string


class ListChannelsResponse(TypedDict, closed=True):
    channels: NotRequired[
        "capo_medialive.types.__list_of_channel_summary.__listOfChannelSummary"
    ]
    next_token: NotRequired["capo_medialive.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelsResponse) -> dict:
    out: dict = {}
    if "channels" in value:
        import capo_medialive.types.__list_of_channel_summary

        out["channels"] = capo_medialive.types.__list_of_channel_summary.serialize_json(
            value["channels"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChannelsResponse:
    out: ListChannelsResponse = {}  # type: ignore[typeddict-item]
    if "channels" in data:
        import capo_medialive.types.__list_of_channel_summary

        out["channels"] = (
            capo_medialive.types.__list_of_channel_summary.deserialize_json(
                data["channels"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
