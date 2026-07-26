"""Generated from Smithy shape ``com.amazonaws.codecommit#PullRequestStatusChangedEventMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.pull_request_status_enum


class PullRequestStatusChangedEventMetadata(TypedDict, closed=True):
    pull_request_status: NotRequired[
        "capo_codecommit.types.pull_request_status_enum.PullRequestStatusEnum"
    ]
    """<p>The changed status of the pull request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PullRequestStatusChangedEventMetadata) -> dict:
    out: dict = {}
    if "pull_request_status" in value:
        import capo_codecommit.types.pull_request_status_enum

        out["pullRequestStatus"] = (
            capo_codecommit.types.pull_request_status_enum.serialize_aws_json_1_1(
                value["pull_request_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PullRequestStatusChangedEventMetadata:
    out: PullRequestStatusChangedEventMetadata = {}  # type: ignore[typeddict-item]
    if "pullRequestStatus" in data:
        import capo_codecommit.types.pull_request_status_enum

        out["pull_request_status"] = (
            capo_codecommit.types.pull_request_status_enum.deserialize_aws_json_1_1(
                data["pullRequestStatus"]
            )
        )
    return out
