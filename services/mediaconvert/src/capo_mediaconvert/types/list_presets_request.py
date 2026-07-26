"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ListPresetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min1_max20
    import capo_mediaconvert.types.__string
    import capo_mediaconvert.types.order
    import capo_mediaconvert.types.preset_list_by


class ListPresetsRequest(TypedDict, closed=True):
    category: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Optionally, specify a preset category to limit responses to only presets from that category."""
    list_by: NotRequired["capo_mediaconvert.types.preset_list_by.PresetListBy"]
    """Optional. When you request a list of presets, you can choose to list them alphabetically by NAME or chronologically by CREATION_DATE. If you don't specify, the service will list them by name."""
    max_results: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
    ]
    """Optional. Number of presets, up to twenty, that will be returned at one time"""
    next_token: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Use this string, provided with the response to a previous request, to request the next batch of presets."""
    order: NotRequired["capo_mediaconvert.types.order.Order"]
    """Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource."""


# --- restJson1 ser/de ---
def serialize_json(value: ListPresetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPresetsRequest:
    out: ListPresetsRequest = {}  # type: ignore[typeddict-item]
    return out
