"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdatePullRequestTitleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecommit.types.pull_request


class UpdatePullRequestTitleOutput(TypedDict, closed=True):
    pull_request: "capo_codecommit.types.pull_request.PullRequest"
    """<p>Information about the updated pull request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePullRequestTitleOutput) -> dict:
    out: dict = {}
    import capo_codecommit.types.pull_request

    out["pullRequest"] = capo_codecommit.types.pull_request.serialize_aws_json_1_1(
        value["pull_request"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePullRequestTitleOutput:
    out: UpdatePullRequestTitleOutput = {}  # type: ignore[typeddict-item]
    if "pullRequest" in data:
        import capo_codecommit.types.pull_request

        out["pull_request"] = (
            capo_codecommit.types.pull_request.deserialize_aws_json_1_1(
                data["pullRequest"]
            )
        )
    else:
        raise DeserializationError("UpdatePullRequestTitleOutput.pull_request required")
    return out
