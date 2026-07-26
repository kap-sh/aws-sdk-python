"""Generated from Smithy shape ``com.amazonaws.mediatailor#ListPlaybackConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__list_of_playback_configuration
    import capo_mediatailor.types.__string


class ListPlaybackConfigurationsResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_mediatailor.types.__list_of_playback_configuration.__listOfPlaybackConfiguration"
    ]
    """<p>Array of playback configurations. This might be all the available configurations or a subset, depending on the settings that you provide and the total number of configurations stored.</p>"""
    next_token: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>Pagination token returned by the GET list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPlaybackConfigurationsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_mediatailor.types.__list_of_playback_configuration

        out["Items"] = (
            capo_mediatailor.types.__list_of_playback_configuration.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPlaybackConfigurationsResponse:
    out: ListPlaybackConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import capo_mediatailor.types.__list_of_playback_configuration

        out["items"] = (
            capo_mediatailor.types.__list_of_playback_configuration.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
