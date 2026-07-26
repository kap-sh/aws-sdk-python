"""Generated from Smithy shape ``com.amazonaws.codecommit#MergePullRequestByThreeWayOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.pull_request


class MergePullRequestByThreeWayOutput(TypedDict, closed=True):
    pull_request: NotRequired["capo_codecommit.types.pull_request.PullRequest"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MergePullRequestByThreeWayOutput) -> dict:
    out: dict = {}
    if "pull_request" in value:
        import capo_codecommit.types.pull_request

        out["pullRequest"] = capo_codecommit.types.pull_request.serialize_aws_json_1_1(
            value["pull_request"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MergePullRequestByThreeWayOutput:
    out: MergePullRequestByThreeWayOutput = {}  # type: ignore[typeddict-item]
    if "pullRequest" in data:
        import capo_codecommit.types.pull_request

        out["pull_request"] = (
            capo_codecommit.types.pull_request.deserialize_aws_json_1_1(
                data["pullRequest"]
            )
        )
    return out
