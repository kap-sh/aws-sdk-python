"""Generated from Smithy shape ``com.amazonaws.medialive#ListChannelsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_channel_summary
    import aws_sdk_medialive.types.__string


class ListChannelsResponse(TypedDict):
    channels: NotRequired[
        "aws_sdk_medialive.types.__list_of_channel_summary.__listOfChannelSummary"
    ]
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelsResponse) -> dict:
    out: dict = {}
    if "channels" in value:
        import aws_sdk_medialive.types.__list_of_channel_summary

        out["channels"] = (
            aws_sdk_medialive.types.__list_of_channel_summary.serialize_json(
                value["channels"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChannelsResponse:
    out: ListChannelsResponse = {}  # type: ignore[typeddict-item]
    if "channels" in data:
        import aws_sdk_medialive.types.__list_of_channel_summary

        out["channels"] = (
            aws_sdk_medialive.types.__list_of_channel_summary.deserialize_json(
                data["channels"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
