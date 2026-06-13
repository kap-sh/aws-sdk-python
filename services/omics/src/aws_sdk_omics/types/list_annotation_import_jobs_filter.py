"""Generated from Smithy shape ``com.amazonaws.omics#ListAnnotationImportJobsFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.job_status


class ListAnnotationImportJobsFilter(TypedDict):
    status: NotRequired["aws_sdk_omics.types.job_status.JobStatus"]
    """<p>A status to filter on.</p>"""
    store_name: NotRequired["str"]
    """<p>A store name to filter on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnnotationImportJobsFilter) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "store_name" in value:
        out["storeName"] = value["store_name"]
    return out


def deserialize_json(data: dict) -> ListAnnotationImportJobsFilter:
    out: ListAnnotationImportJobsFilter = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    if "storeName" in data:
        out["store_name"] = data["storeName"]
    return out
