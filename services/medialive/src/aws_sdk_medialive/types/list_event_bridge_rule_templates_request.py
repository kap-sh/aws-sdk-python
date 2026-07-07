"""Generated from Smithy shape ``com.amazonaws.medialive#ListEventBridgeRuleTemplatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.max_results


class ListEventBridgeRuleTemplatesRequest(TypedDict, closed=True):
    group_identifier: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """An eventbridge rule template group's identifier. Can be either be its id or current name."""
    max_results: NotRequired["aws_sdk_medialive.types.max_results.MaxResults"]
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """A token used to retrieve the next set of results in paginated list responses."""
    signal_map_identifier: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """A signal map's identifier. Can be either be its id or current name."""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventBridgeRuleTemplatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEventBridgeRuleTemplatesRequest:
    out: ListEventBridgeRuleTemplatesRequest = {}  # type: ignore[typeddict-item]
    return out
