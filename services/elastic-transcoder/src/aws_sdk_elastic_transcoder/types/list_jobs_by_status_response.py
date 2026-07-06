"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#ListJobsByStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.id
    import aws_sdk_elastic_transcoder.types.jobs


class ListJobsByStatusResponse(TypedDict, closed=True):
    jobs: NotRequired["aws_sdk_elastic_transcoder.types.jobs.Jobs"]
    """<p>An array of <code>Job</code> objects that have the specified status.</p>"""
    next_page_token: NotRequired["aws_sdk_elastic_transcoder.types.id.Id"]
    """<p> A value that you use to access the second and subsequent pages of results, if any. When the jobs in the specified pipeline fit on one page or when you've reached the last page of results, the value of <code>NextPageToken</code> is <code>null</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsByStatusResponse) -> dict:
    out: dict = {}
    if "jobs" in value:
        import aws_sdk_elastic_transcoder.types.jobs

        out["Jobs"] = aws_sdk_elastic_transcoder.types.jobs.serialize_json(
            value["jobs"]
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_json(data: dict) -> ListJobsByStatusResponse:
    out: ListJobsByStatusResponse = {}  # type: ignore[typeddict-item]
    if "Jobs" in data:
        import aws_sdk_elastic_transcoder.types.jobs

        out["jobs"] = aws_sdk_elastic_transcoder.types.jobs.deserialize_json(
            data["Jobs"]
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
