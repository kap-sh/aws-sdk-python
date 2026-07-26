"""Generated from Smithy shape ``com.amazonaws.codecommit#ListPullRequestsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecommit.types.next_token
    import capo_codecommit.types.pull_request_id_list


class ListPullRequestsOutput(TypedDict, closed=True):
    pull_request_ids: "capo_codecommit.types.pull_request_id_list.PullRequestIdList"
    """<p>The system-generated IDs of the pull requests.</p>"""
    next_token: NotRequired["capo_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that allows the operation to batch the next results of the operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPullRequestsOutput) -> dict:
    out: dict = {}
    import capo_codecommit.types.pull_request_id_list

    out["pullRequestIds"] = (
        capo_codecommit.types.pull_request_id_list.serialize_aws_json_1_1(
            value["pull_request_ids"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPullRequestsOutput:
    out: ListPullRequestsOutput = {}  # type: ignore[typeddict-item]
    if "pullRequestIds" in data:
        import capo_codecommit.types.pull_request_id_list

        out["pull_request_ids"] = (
            capo_codecommit.types.pull_request_id_list.deserialize_aws_json_1_1(
                data["pullRequestIds"]
            )
        )
    else:
        raise DeserializationError("ListPullRequestsOutput.pull_request_ids required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
