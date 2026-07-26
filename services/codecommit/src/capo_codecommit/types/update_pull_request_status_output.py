"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdatePullRequestStatusOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecommit.types.pull_request


class UpdatePullRequestStatusOutput(TypedDict, closed=True):
    pull_request: "capo_codecommit.types.pull_request.PullRequest"
    """<p>Information about the pull request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePullRequestStatusOutput) -> dict:
    out: dict = {}
    import capo_codecommit.types.pull_request

    out["pullRequest"] = capo_codecommit.types.pull_request.serialize_aws_json_1_1(
        value["pull_request"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePullRequestStatusOutput:
    out: UpdatePullRequestStatusOutput = {}  # type: ignore[typeddict-item]
    if "pullRequest" in data:
        import capo_codecommit.types.pull_request

        out["pull_request"] = (
            capo_codecommit.types.pull_request.deserialize_aws_json_1_1(
                data["pullRequest"]
            )
        )
    else:
        raise DeserializationError(
            "UpdatePullRequestStatusOutput.pull_request required"
        )
    return out
