"""Generated from Smithy shape ``com.amazonaws.amplify#StopJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplify.types.app_id
    import aws_sdk_amplify.types.branch_name
    import aws_sdk_amplify.types.job_id


class StopJobRequest(TypedDict, closed=True):
    app_id: "aws_sdk_amplify.types.app_id.AppId"
    """<p> The unique ID for an Amplify app. </p>"""
    branch_name: "aws_sdk_amplify.types.branch_name.BranchName"
    """<p>The name of the branch to use for the stop job request. </p>"""
    job_id: "aws_sdk_amplify.types.job_id.JobId"
    """<p> The unique id for the job. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopJobRequest:
    out: StopJobRequest = {}  # type: ignore[typeddict-item]
    return out
