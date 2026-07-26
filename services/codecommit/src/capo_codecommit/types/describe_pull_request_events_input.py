"""Generated from Smithy shape ``com.amazonaws.codecommit#DescribePullRequestEventsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecommit.types.arn
    import capo_codecommit.types.max_results
    import capo_codecommit.types.next_token
    import capo_codecommit.types.pull_request_event_type
    import capo_codecommit.types.pull_request_id


class DescribePullRequestEventsInput(TypedDict, closed=True):
    pull_request_id: "capo_codecommit.types.pull_request_id.PullRequestId"
    """<p>The system-generated ID of the pull request. To get this ID, use <a>ListPullRequests</a>.</p>"""
    pull_request_event_type: NotRequired[
        "capo_codecommit.types.pull_request_event_type.PullRequestEventType"
    ]
    """<p>Optional. The pull request event type about which you want to return information.</p>"""
    actor_arn: NotRequired["capo_codecommit.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the user whose actions resulted in the event. Examples include updating the pull request with more commits or changing the status of a pull request.</p>"""
    next_token: NotRequired["capo_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>"""
    max_results: NotRequired["capo_codecommit.types.max_results.MaxResults"]
    """<p>A non-zero, non-negative integer used to limit the number of returned results. The default is 100 events, which is also the maximum number of events that can be returned in a result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePullRequestEventsInput) -> dict:
    out: dict = {}
    out["pullRequestId"] = value["pull_request_id"]
    if "pull_request_event_type" in value:
        import capo_codecommit.types.pull_request_event_type

        out["pullRequestEventType"] = (
            capo_codecommit.types.pull_request_event_type.serialize_aws_json_1_1(
                value["pull_request_event_type"]
            )
        )
    if "actor_arn" in value:
        out["actorArn"] = value["actor_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePullRequestEventsInput:
    out: DescribePullRequestEventsInput = {}  # type: ignore[typeddict-item]
    if "pullRequestId" in data:
        out["pull_request_id"] = data["pullRequestId"]
    else:
        raise DeserializationError(
            "DescribePullRequestEventsInput.pull_request_id required"
        )
    if "pullRequestEventType" in data:
        import capo_codecommit.types.pull_request_event_type

        out["pull_request_event_type"] = (
            capo_codecommit.types.pull_request_event_type.deserialize_aws_json_1_1(
                data["pullRequestEventType"]
            )
        )
    if "actorArn" in data:
        out["actor_arn"] = data["actorArn"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
