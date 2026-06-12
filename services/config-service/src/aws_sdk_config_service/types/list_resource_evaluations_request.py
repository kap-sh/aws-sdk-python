"""Generated from Smithy shape ``com.amazonaws.configservice#ListResourceEvaluationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.list_resource_evaluations_page_item_limit
    import aws_sdk_config_service.types.resource_evaluation_filters
    import aws_sdk_config_service.types.string


class ListResourceEvaluationsRequest(TypedDict):
    filters: NotRequired[
        "aws_sdk_config_service.types.resource_evaluation_filters.ResourceEvaluationFilters"
    ]
    """<p>Returns a <code>ResourceEvaluationFilters</code> object.</p>"""
    limit: "aws_sdk_config_service.types.list_resource_evaluations_page_item_limit.ListResourceEvaluationsPageItemLimit"
    """<p>The maximum number of evaluations returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, Config uses the default.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourceEvaluationsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_config_service.types.resource_evaluation_filters

        out["Filters"] = (
            aws_sdk_config_service.types.resource_evaluation_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    out["Limit"] = value.get("limit", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourceEvaluationsRequest:
    out: ListResourceEvaluationsRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_config_service.types.resource_evaluation_filters

        out["filters"] = (
            aws_sdk_config_service.types.resource_evaluation_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
