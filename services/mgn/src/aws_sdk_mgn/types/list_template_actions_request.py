"""Generated from Smithy shape ``com.amazonaws.mgn#ListTemplateActionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.launch_configuration_template_id
    import aws_sdk_mgn.types.max_results_type
    import aws_sdk_mgn.types.pagination_token
    import aws_sdk_mgn.types.template_actions_request_filters


class ListTemplateActionsRequest(TypedDict):
    launch_configuration_template_id: "aws_sdk_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID"
    """<p>Launch configuration template ID.</p>"""
    filters: NotRequired[
        "aws_sdk_mgn.types.template_actions_request_filters.TemplateActionsRequestFilters"
    ]
    """<p>Filters to apply when listing template post migration custom actions.</p>"""
    max_results: NotRequired["aws_sdk_mgn.types.max_results_type.MaxResultsType"]
    """<p>Maximum amount of items to return when listing template post migration custom actions.</p>"""
    next_token: NotRequired["aws_sdk_mgn.types.pagination_token.PaginationToken"]
    """<p>Next token to use when listing template post migration custom actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplateActionsRequest) -> dict:
    out: dict = {}
    out["launchConfigurationTemplateID"] = value["launch_configuration_template_id"]
    if "filters" in value:
        import aws_sdk_mgn.types.template_actions_request_filters

        out["filters"] = (
            aws_sdk_mgn.types.template_actions_request_filters.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTemplateActionsRequest:
    out: ListTemplateActionsRequest = {}  # type: ignore[typeddict-item]
    if "launchConfigurationTemplateID" in data:
        out["launch_configuration_template_id"] = data["launchConfigurationTemplateID"]
    else:
        raise DeserializationError(
            "ListTemplateActionsRequest.launch_configuration_template_id required"
        )
    if "filters" in data:
        import aws_sdk_mgn.types.template_actions_request_filters

        out["filters"] = (
            aws_sdk_mgn.types.template_actions_request_filters.deserialize_json(
                data["filters"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
