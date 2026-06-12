"""Generated from Smithy shape ``com.amazonaws.codestarconnections#ListConnectionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codestar_connections.types.host_arn
    import aws_sdk_codestar_connections.types.max_results
    import aws_sdk_codestar_connections.types.next_token
    import aws_sdk_codestar_connections.types.provider_type


class ListConnectionsInput(TypedDict):
    provider_type_filter: NotRequired[
        "aws_sdk_codestar_connections.types.provider_type.ProviderType"
    ]
    """<p>Filters the list of connections to those associated with a specified provider, such as Bitbucket.</p>"""
    host_arn_filter: NotRequired["aws_sdk_codestar_connections.types.host_arn.HostArn"]
    """<p>Filters the list of connections to those associated with a specified host.</p>"""
    max_results: "aws_sdk_codestar_connections.types.max_results.MaxResults"
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_codestar_connections.types.next_token.NextToken"]
    """<p>The token that was returned from the previous <code>ListConnections</code> call, which can be used to return the next set of connections in the list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListConnectionsInput) -> dict:
    out: dict = {}
    if "provider_type_filter" in value:
        import aws_sdk_codestar_connections.types.provider_type

        out["ProviderTypeFilter"] = (
            aws_sdk_codestar_connections.types.provider_type.serialize_aws_json_1_0(
                value["provider_type_filter"]
            )
        )
    if "host_arn_filter" in value:
        out["HostArnFilter"] = value["host_arn_filter"]
    out["MaxResults"] = value.get("max_results", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListConnectionsInput:
    out: ListConnectionsInput = {}  # type: ignore[typeddict-item]
    if "ProviderTypeFilter" in data:
        import aws_sdk_codestar_connections.types.provider_type

        out["provider_type_filter"] = (
            aws_sdk_codestar_connections.types.provider_type.deserialize_aws_json_1_0(
                data["ProviderTypeFilter"]
            )
        )
    if "HostArnFilter" in data:
        out["host_arn_filter"] = data["HostArnFilter"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
