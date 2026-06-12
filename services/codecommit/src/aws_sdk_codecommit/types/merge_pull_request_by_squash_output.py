"""Generated from Smithy shape ``com.amazonaws.codecommit#MergePullRequestBySquashOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.pull_request


class MergePullRequestBySquashOutput(TypedDict):
    pull_request: NotRequired["aws_sdk_codecommit.types.pull_request.PullRequest"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MergePullRequestBySquashOutput) -> dict:
    out: dict = {}
    if "pull_request" in value:
        import aws_sdk_codecommit.types.pull_request

        out["pullRequest"] = (
            aws_sdk_codecommit.types.pull_request.serialize_aws_json_1_1(
                value["pull_request"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MergePullRequestBySquashOutput:
    out: MergePullRequestBySquashOutput = {}  # type: ignore[typeddict-item]
    if "pullRequest" in data:
        import aws_sdk_codecommit.types.pull_request

        out["pull_request"] = (
            aws_sdk_codecommit.types.pull_request.deserialize_aws_json_1_1(
                data["pullRequest"]
            )
        )
    return out
