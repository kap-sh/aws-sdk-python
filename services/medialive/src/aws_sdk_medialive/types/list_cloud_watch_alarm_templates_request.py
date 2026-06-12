"""Generated from Smithy shape ``com.amazonaws.medialive#ListCloudWatchAlarmTemplatesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.max_results


class ListCloudWatchAlarmTemplatesRequest(TypedDict):
    group_identifier: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """A cloudwatch alarm template group's identifier. Can be either be its id or current name."""
    max_results: NotRequired["aws_sdk_medialive.types.max_results.MaxResults"]
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """A token used to retrieve the next set of results in paginated list responses."""
    scope: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Represents the scope of a resource, with options for all scopes, AWS provided resources, or local resources."""
    signal_map_identifier: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """A signal map's identifier. Can be either be its id or current name."""


# --- restJson1 ser/de ---
def serialize_json(value: ListCloudWatchAlarmTemplatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCloudWatchAlarmTemplatesRequest:
    out: ListCloudWatchAlarmTemplatesRequest = {}  # type: ignore[typeddict-item]
    return out
