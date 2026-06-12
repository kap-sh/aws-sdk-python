"""Generated from Smithy shape ``com.amazonaws.connect#GetCurrentUserDataRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.max_result100
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.user_data_filters


class GetCurrentUserDataRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    filters: "aws_sdk_connect.types.user_data_filters.UserDataFilters"
    """<p>The filters to apply to returned user data. You can filter up to the following limits:</p> <ul> <li> <p>Queues: 100</p> </li> <li> <p>Routing profiles: 100</p> </li> <li> <p>Agents: 100</p> </li> <li> <p>Contact states: 9</p> </li> <li> <p>User hierarchy groups: 1</p> </li> </ul> <p> The user data is retrieved for only the specified values/resources in the filter. A maximum of one filter can be passed from queues, routing profiles, agents, and user hierarchy groups. </p> <p>Currently tagging is only supported on the resources that are passed in the filter.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_connect.types.max_result100.MaxResult100"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCurrentUserDataRequest) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.user_data_filters

    out["Filters"] = aws_sdk_connect.types.user_data_filters.serialize_json(
        value["filters"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> GetCurrentUserDataRequest:
    out: GetCurrentUserDataRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_connect.types.user_data_filters

        out["filters"] = aws_sdk_connect.types.user_data_filters.deserialize_json(
            data["Filters"]
        )
    else:
        raise DeserializationError("GetCurrentUserDataRequest.filters required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
