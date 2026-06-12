"""Generated from Smithy shape ``com.amazonaws.panorama#ListNodeFromTemplateJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.next_token
    import aws_sdk_panorama.types.node_from_template_job_list


class ListNodeFromTemplateJobsResponse(TypedDict):
    node_from_template_jobs: (
        "aws_sdk_panorama.types.node_from_template_job_list.NodeFromTemplateJobList"
    )
    """<p>A list of jobs.</p>"""
    next_token: NotRequired["aws_sdk_panorama.types.next_token.NextToken"]
    """<p>A pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNodeFromTemplateJobsResponse) -> dict:
    out: dict = {}
    import aws_sdk_panorama.types.node_from_template_job_list

    out["NodeFromTemplateJobs"] = (
        aws_sdk_panorama.types.node_from_template_job_list.serialize_json(
            value["node_from_template_jobs"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNodeFromTemplateJobsResponse:
    out: ListNodeFromTemplateJobsResponse = {}  # type: ignore[typeddict-item]
    if "NodeFromTemplateJobs" in data:
        import aws_sdk_panorama.types.node_from_template_job_list

        out["node_from_template_jobs"] = (
            aws_sdk_panorama.types.node_from_template_job_list.deserialize_json(
                data["NodeFromTemplateJobs"]
            )
        )
    else:
        raise DeserializationError(
            "ListNodeFromTemplateJobsResponse.node_from_template_jobs required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
