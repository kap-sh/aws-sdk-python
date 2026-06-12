"""Generated from Smithy shape ``com.amazonaws.medicalimaging#ListDICOMImportJobsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.datastore_id
    import aws_sdk_medical_imaging.types.job_status
    import aws_sdk_medical_imaging.types.next_token


class ListDICOMImportJobsRequest(TypedDict):
    datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    job_status: NotRequired["aws_sdk_medical_imaging.types.job_status.JobStatus"]
    """<p>The filters for listing import jobs based on status.</p>"""
    next_token: NotRequired["aws_sdk_medical_imaging.types.next_token.NextToken"]
    """<p>The pagination token used to request the list of import jobs on the next page.</p>"""
    max_results: NotRequired["int"]
    """<p>The max results count. The upper bound is determined by load testing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDICOMImportJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDICOMImportJobsRequest:
    out: ListDICOMImportJobsRequest = {}  # type: ignore[typeddict-item]
    return out
