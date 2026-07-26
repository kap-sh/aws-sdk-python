"""Generated from Smithy shape ``com.amazonaws.amplifybackend#ListBackendJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__string
    import capo_amplifybackend.types.list_of_backend_job_resp_obj


class ListBackendJobsResponse(TypedDict, closed=True):
    jobs: NotRequired[
        "capo_amplifybackend.types.list_of_backend_job_resp_obj.ListOfBackendJobRespObj"
    ]
    """<p>An array of jobs and their properties.</p>"""
    next_token: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBackendJobsResponse) -> dict:
    out: dict = {}
    if "jobs" in value:
        import capo_amplifybackend.types.list_of_backend_job_resp_obj

        out["jobs"] = (
            capo_amplifybackend.types.list_of_backend_job_resp_obj.serialize_json(
                value["jobs"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBackendJobsResponse:
    out: ListBackendJobsResponse = {}  # type: ignore[typeddict-item]
    if "jobs" in data:
        import capo_amplifybackend.types.list_of_backend_job_resp_obj

        out["jobs"] = (
            capo_amplifybackend.types.list_of_backend_job_resp_obj.deserialize_json(
                data["jobs"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
