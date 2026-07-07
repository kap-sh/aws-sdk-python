"""Generated from Smithy shape ``com.amazonaws.cloud9#ListEnvironmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloud9.types.max_results
    import aws_sdk_cloud9.types.string


class ListEnvironmentsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_cloud9.types.string.String"]
    """<p>During a previous call, if there are more than 25 items in the list, only the first 25 items are returned, along with a unique string called a <i>next token</i>. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.</p>"""
    max_results: NotRequired["aws_sdk_cloud9.types.max_results.MaxResults"]
    """<p>The maximum number of environments to get identifiers for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEnvironmentsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEnvironmentsRequest:
    out: ListEnvironmentsRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
