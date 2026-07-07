"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListImportFailuresRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.list_import_failures_max_results_count
    import aws_sdk_cloudtrail.types.pagination_token
    import aws_sdk_cloudtrail.types.uuid


class ListImportFailuresRequest(TypedDict, closed=True):
    import_id: "aws_sdk_cloudtrail.types.uuid.UUID"
    """<p> The ID of the import. </p>"""
    max_results: NotRequired[
        "aws_sdk_cloudtrail.types.list_import_failures_max_results_count.ListImportFailuresMaxResultsCount"
    ]
    """<p> The maximum number of failures to display on a single page. </p>"""
    next_token: NotRequired["aws_sdk_cloudtrail.types.pagination_token.PaginationToken"]
    """<p> A token you can use to get the next page of import failures. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListImportFailuresRequest) -> dict:
    out: dict = {}
    out["ImportId"] = value["import_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListImportFailuresRequest:
    out: ListImportFailuresRequest = {}  # type: ignore[typeddict-item]
    if "ImportId" in data:
        out["import_id"] = data["ImportId"]
    else:
        raise DeserializationError("ListImportFailuresRequest.import_id required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
