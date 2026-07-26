"""Generated from Smithy shape ``com.amazonaws.codecommit#DescribePullRequestEventsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecommit.types.next_token
    import capo_codecommit.types.pull_request_event_list


class DescribePullRequestEventsOutput(TypedDict, closed=True):
    pull_request_events: (
        "capo_codecommit.types.pull_request_event_list.PullRequestEventList"
    )
    """<p>Information about the pull request events.</p>"""
    next_token: NotRequired["capo_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that can be used in a request to return the next batch of the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePullRequestEventsOutput) -> dict:
    out: dict = {}
    import capo_codecommit.types.pull_request_event_list

    out["pullRequestEvents"] = (
        capo_codecommit.types.pull_request_event_list.serialize_aws_json_1_1(
            value["pull_request_events"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePullRequestEventsOutput:
    out: DescribePullRequestEventsOutput = {}  # type: ignore[typeddict-item]
    if "pullRequestEvents" in data:
        import capo_codecommit.types.pull_request_event_list

        out["pull_request_events"] = (
            capo_codecommit.types.pull_request_event_list.deserialize_aws_json_1_1(
                data["pullRequestEvents"]
            )
        )
    else:
        raise DeserializationError(
            "DescribePullRequestEventsOutput.pull_request_events required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
