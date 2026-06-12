"""Generated from Smithy shape ``com.amazonaws.codecommit#GetPullRequestOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.pull_request


class GetPullRequestOutput(TypedDict):
    pull_request: "aws_sdk_codecommit.types.pull_request.PullRequest"
    """<p>Information about the specified pull request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPullRequestOutput) -> dict:
    out: dict = {}
    import aws_sdk_codecommit.types.pull_request

    out["pullRequest"] = aws_sdk_codecommit.types.pull_request.serialize_aws_json_1_1(
        value["pull_request"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPullRequestOutput:
    out: GetPullRequestOutput = {}  # type: ignore[typeddict-item]
    if "pullRequest" in data:
        import aws_sdk_codecommit.types.pull_request

        out["pull_request"] = (
            aws_sdk_codecommit.types.pull_request.deserialize_aws_json_1_1(
                data["pullRequest"]
            )
        )
    else:
        raise DeserializationError("GetPullRequestOutput.pull_request required")
    return out
