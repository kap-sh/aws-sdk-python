"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SearchFlowTemplatesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.flow_template_filters
    import aws_sdk_iotthingsgraph.types.max_results
    import aws_sdk_iotthingsgraph.types.next_token


class SearchFlowTemplatesRequest(TypedDict):
    filters: NotRequired[
        "aws_sdk_iotthingsgraph.types.flow_template_filters.FlowTemplateFilters"
    ]
    """<p>An array of objects that limit the result set. The only valid filter is <code>DEVICE_MODEL_ID</code>.</p>"""
    next_token: NotRequired["aws_sdk_iotthingsgraph.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results. Use this when you're paginating results.</p>"""
    max_results: NotRequired["aws_sdk_iotthingsgraph.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchFlowTemplatesRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_iotthingsgraph.types.flow_template_filters

        out["filters"] = (
            aws_sdk_iotthingsgraph.types.flow_template_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchFlowTemplatesRequest:
    out: SearchFlowTemplatesRequest = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_iotthingsgraph.types.flow_template_filters

        out["filters"] = (
            aws_sdk_iotthingsgraph.types.flow_template_filters.deserialize_aws_json_1_1(
                data["filters"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
