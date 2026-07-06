"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeSessionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.next_token
    import aws_sdk_ssm.types.session_filter_list
    import aws_sdk_ssm.types.session_max_results
    import aws_sdk_ssm.types.session_state


class DescribeSessionsRequest(TypedDict, closed=True):
    state: "aws_sdk_ssm.types.session_state.SessionState"
    r"""<p>The session status to retrieve a list of sessions for. For example, \"Active\".</p>"""
    max_results: NotRequired["aws_sdk_ssm.types.session_max_results.SessionMaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    filters: NotRequired["aws_sdk_ssm.types.session_filter_list.SessionFilterList"]
    """<p>One or more filters to limit the type of sessions returned by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSessionsRequest) -> dict:
    out: dict = {}
    import aws_sdk_ssm.types.session_state

    out["State"] = aws_sdk_ssm.types.session_state.serialize_aws_json_1_1(
        value["state"]
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import aws_sdk_ssm.types.session_filter_list

        out["Filters"] = aws_sdk_ssm.types.session_filter_list.serialize_aws_json_1_1(
            value["filters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSessionsRequest:
    out: DescribeSessionsRequest = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import aws_sdk_ssm.types.session_state

        out["state"] = aws_sdk_ssm.types.session_state.deserialize_aws_json_1_1(
            data["State"]
        )
    else:
        raise DeserializationError("DescribeSessionsRequest.state required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Filters" in data:
        import aws_sdk_ssm.types.session_filter_list

        out["filters"] = aws_sdk_ssm.types.session_filter_list.deserialize_aws_json_1_1(
            data["Filters"]
        )
    return out
