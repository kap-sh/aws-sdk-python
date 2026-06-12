"""Generated from Smithy shape ``com.amazonaws.medialive#ListSignalMapsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.max_results


class ListSignalMapsRequest(TypedDict):
    cloud_watch_alarm_template_group_identifier: NotRequired[
        "aws_sdk_medialive.types.__string.__string"
    ]
    """A cloudwatch alarm template group's identifier. Can be either be its id or current name."""
    event_bridge_rule_template_group_identifier: NotRequired[
        "aws_sdk_medialive.types.__string.__string"
    ]
    """An eventbridge rule template group's identifier. Can be either be its id or current name."""
    max_results: NotRequired["aws_sdk_medialive.types.max_results.MaxResults"]
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """A token used to retrieve the next set of results in paginated list responses."""


# --- restJson1 ser/de ---
def serialize_json(value: ListSignalMapsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSignalMapsRequest:
    out: ListSignalMapsRequest = {}  # type: ignore[typeddict-item]
    return out
