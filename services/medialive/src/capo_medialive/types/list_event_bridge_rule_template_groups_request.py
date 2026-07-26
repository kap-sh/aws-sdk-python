"""Generated from Smithy shape ``com.amazonaws.medialive#ListEventBridgeRuleTemplateGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.max_results


class ListEventBridgeRuleTemplateGroupsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_medialive.types.max_results.MaxResults"]
    next_token: NotRequired["capo_medialive.types.__string.__string"]
    """A token used to retrieve the next set of results in paginated list responses."""
    signal_map_identifier: NotRequired["capo_medialive.types.__string.__string"]
    """A signal map's identifier. Can be either be its id or current name."""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventBridgeRuleTemplateGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEventBridgeRuleTemplateGroupsRequest:
    out: ListEventBridgeRuleTemplateGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
