"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ListConnectionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.connection_response_list
    import aws_sdk_cloudwatch_events.types.next_token


class ListConnectionsResponse(TypedDict, closed=True):
    connections: NotRequired[
        "aws_sdk_cloudwatch_events.types.connection_response_list.ConnectionResponseList"
    ]
    """<p>An array of connections objects that include details about the connections.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_events.types.next_token.NextToken"]
    """<p>A token you can use in a subsequent request to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListConnectionsResponse) -> dict:
    out: dict = {}
    if "connections" in value:
        import aws_sdk_cloudwatch_events.types.connection_response_list

        out["Connections"] = (
            aws_sdk_cloudwatch_events.types.connection_response_list.serialize_aws_json_1_1(
                value["connections"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListConnectionsResponse:
    out: ListConnectionsResponse = {}  # type: ignore[typeddict-item]
    if "Connections" in data:
        import aws_sdk_cloudwatch_events.types.connection_response_list

        out["connections"] = (
            aws_sdk_cloudwatch_events.types.connection_response_list.deserialize_aws_json_1_1(
                data["Connections"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
