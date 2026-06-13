"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListMLInputChannelsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.ml_input_channels_list
    import aws_sdk_cleanroomsml.types.next_token


class ListMLInputChannelsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    ml_input_channels_list: (
        "aws_sdk_cleanroomsml.types.ml_input_channels_list.MLInputChannelsList"
    )
    """<p>The list of ML input channels that you wanted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMLInputChannelsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_cleanroomsml.types.ml_input_channels_list

    out["mlInputChannelsList"] = (
        aws_sdk_cleanroomsml.types.ml_input_channels_list.serialize_json(
            value["ml_input_channels_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListMLInputChannelsResponse:
    out: ListMLInputChannelsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "mlInputChannelsList" in data:
        import aws_sdk_cleanroomsml.types.ml_input_channels_list

        out["ml_input_channels_list"] = (
            aws_sdk_cleanroomsml.types.ml_input_channels_list.deserialize_json(
                data["mlInputChannelsList"]
            )
        )
    else:
        raise DeserializationError(
            "ListMLInputChannelsResponse.ml_input_channels_list required"
        )
    return out
