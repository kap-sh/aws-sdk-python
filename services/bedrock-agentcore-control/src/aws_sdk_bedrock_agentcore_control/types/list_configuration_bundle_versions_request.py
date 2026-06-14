"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListConfigurationBundleVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id
    import aws_sdk_bedrock_agentcore_control.types.version_filter


class ListConfigurationBundleVersionsRequest(TypedDict):
    bundle_id: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId"
    """<p>The unique identifier of the configuration bundle to list versions for.</p>"""
    next_token: NotRequired["str"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""
    filter: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.version_filter.VersionFilter"
    ]
    """<p>An optional filter for listing versions, including branch name, creation source, and whether to return only the latest version per branch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationBundleVersionsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_bedrock_agentcore_control.types.version_filter

        out["filter"] = (
            aws_sdk_bedrock_agentcore_control.types.version_filter.serialize_json(
                value["filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListConfigurationBundleVersionsRequest:
    out: ListConfigurationBundleVersionsRequest = {}  # type: ignore[typeddict-item]
    if "filter" in data:
        import aws_sdk_bedrock_agentcore_control.types.version_filter

        out["filter"] = (
            aws_sdk_bedrock_agentcore_control.types.version_filter.deserialize_json(
                data["filter"]
            )
        )
    return out
