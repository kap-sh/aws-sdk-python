"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ListCodegenJobsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.app_id
    import aws_sdk_amplifyuibuilder.types.list_codegen_jobs_limit


class ListCodegenJobsRequest(TypedDict):
    app_id: "aws_sdk_amplifyuibuilder.types.app_id.AppId"
    """<p>The unique ID for the Amplify app.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is a part of the Amplify app.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to request the next page of results.</p>"""
    max_results: (
        "aws_sdk_amplifyuibuilder.types.list_codegen_jobs_limit.ListCodegenJobsLimit"
    )
    """<p>The maximum number of jobs to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCodegenJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCodegenJobsRequest:
    out: ListCodegenJobsRequest = {}  # type: ignore[typeddict-item]
    return out
