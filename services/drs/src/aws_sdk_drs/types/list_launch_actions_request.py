"""Generated from Smithy shape ``com.amazonaws.drs#ListLaunchActionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_drs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.launch_action_resource_id
    import aws_sdk_drs.types.launch_actions_request_filters
    import aws_sdk_drs.types.max_results_type
    import aws_sdk_drs.types.pagination_token


class ListLaunchActionsRequest(TypedDict):
    resource_id: "aws_sdk_drs.types.launch_action_resource_id.LaunchActionResourceId"
    filters: NotRequired[
        "aws_sdk_drs.types.launch_actions_request_filters.LaunchActionsRequestFilters"
    ]
    """<p>Filters to apply when listing resource launch actions.</p>"""
    max_results: NotRequired["aws_sdk_drs.types.max_results_type.MaxResultsType"]
    """<p>Maximum amount of items to return when listing resource launch actions.</p>"""
    next_token: NotRequired["aws_sdk_drs.types.pagination_token.PaginationToken"]
    """<p>Next token to use when listing resource launch actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLaunchActionsRequest) -> dict:
    out: dict = {}
    out["resourceId"] = value["resource_id"]
    if "filters" in value:
        import aws_sdk_drs.types.launch_actions_request_filters

        out["filters"] = (
            aws_sdk_drs.types.launch_actions_request_filters.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLaunchActionsRequest:
    out: ListLaunchActionsRequest = {}  # type: ignore[typeddict-item]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("ListLaunchActionsRequest.resource_id required")
    if "filters" in data:
        import aws_sdk_drs.types.launch_actions_request_filters

        out["filters"] = (
            aws_sdk_drs.types.launch_actions_request_filters.deserialize_json(
                data["filters"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
