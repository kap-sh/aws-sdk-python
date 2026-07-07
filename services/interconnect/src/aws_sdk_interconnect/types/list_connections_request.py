"""Generated from Smithy shape ``com.amazonaws.interconnect#ListConnectionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_interconnect.types.attach_point
    import aws_sdk_interconnect.types.connection_state
    import aws_sdk_interconnect.types.environment_id
    import aws_sdk_interconnect.types.max_results
    import aws_sdk_interconnect.types.next_token
    import aws_sdk_interconnect.types.provider


class ListConnectionsRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_interconnect.types.max_results.MaxResults"]
    """<p>The max number of list results in a single paginated response.</p>"""
    next_token: NotRequired["aws_sdk_interconnect.types.next_token.NextToken"]
    """<p>A pagination token from a previous paginated response indicating you wish to get the next page of results.</p>"""
    state: NotRequired["aws_sdk_interconnect.types.connection_state.ConnectionState"]
    """<p>Filter the results to only include <a>Connection</a> objects in the given <a>Connection$state</a>.</p>"""
    environment_id: NotRequired[
        "aws_sdk_interconnect.types.environment_id.EnvironmentId"
    ]
    """<p>Filter the results to only include <a>Connection</a> objects on the given <a>Environment</a>.</p>"""
    provider: NotRequired["aws_sdk_interconnect.types.provider.Provider"]
    """<p>Filter the results to only include <a>Connection</a> objects to the given <a>Provider</a>.</p>"""
    attach_point: NotRequired["aws_sdk_interconnect.types.attach_point.AttachPoint"]
    """<p>Filter results to only include <a>Connection</a> objects attached to the given <a>AttachPoint</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListConnectionsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "state" in value:
        import aws_sdk_interconnect.types.connection_state

        out["state"] = (
            aws_sdk_interconnect.types.connection_state.serialize_aws_json_1_0(
                value["state"]
            )
        )
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "provider" in value:
        import aws_sdk_interconnect.types.provider

        out["provider"] = aws_sdk_interconnect.types.provider.serialize_aws_json_1_0(
            value["provider"]
        )
    if "attach_point" in value:
        import aws_sdk_interconnect.types.attach_point

        out["attachPoint"] = (
            aws_sdk_interconnect.types.attach_point.serialize_aws_json_1_0(
                value["attach_point"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListConnectionsRequest:
    out: ListConnectionsRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "state" in data:
        import aws_sdk_interconnect.types.connection_state

        out["state"] = (
            aws_sdk_interconnect.types.connection_state.deserialize_aws_json_1_0(
                data["state"]
            )
        )
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "provider" in data:
        import aws_sdk_interconnect.types.provider

        out["provider"] = aws_sdk_interconnect.types.provider.deserialize_aws_json_1_0(
            data["provider"]
        )
    if "attachPoint" in data:
        import aws_sdk_interconnect.types.attach_point

        out["attach_point"] = (
            aws_sdk_interconnect.types.attach_point.deserialize_aws_json_1_0(
                data["attachPoint"]
            )
        )
    return out
