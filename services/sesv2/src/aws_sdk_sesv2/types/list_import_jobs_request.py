"""Generated from Smithy shape ``com.amazonaws.sesv2#ListImportJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.import_destination_type
    import aws_sdk_sesv2.types.max_items
    import aws_sdk_sesv2.types.next_token


class ListImportJobsRequest(TypedDict, closed=True):
    import_destination_type: NotRequired[
        "aws_sdk_sesv2.types.import_destination_type.ImportDestinationType"
    ]
    """<p>The destination of the import job, which can be used to list import jobs that have a certain <code>ImportDestinationType</code>.</p>"""
    next_token: NotRequired["aws_sdk_sesv2.types.next_token.NextToken"]
    """<p>A string token indicating that there might be additional import jobs available to be listed. Copy this token to a subsequent call to <code>ListImportJobs</code> with the same parameters to retrieve the next page of import jobs.</p>"""
    page_size: NotRequired["aws_sdk_sesv2.types.max_items.MaxItems"]
    """<p>Maximum number of import jobs to return at once. Use this parameter to paginate results. If additional import jobs exist beyond the specified limit, the <code>NextToken</code> element is sent in the response. Use the <code>NextToken</code> value in subsequent requests to retrieve additional addresses.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImportJobsRequest) -> dict:
    out: dict = {}
    if "import_destination_type" in value:
        import aws_sdk_sesv2.types.import_destination_type

        out["ImportDestinationType"] = (
            aws_sdk_sesv2.types.import_destination_type.serialize_json(
                value["import_destination_type"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    return out


def deserialize_json(data: dict) -> ListImportJobsRequest:
    out: ListImportJobsRequest = {}  # type: ignore[typeddict-item]
    if "ImportDestinationType" in data:
        import aws_sdk_sesv2.types.import_destination_type

        out["import_destination_type"] = (
            aws_sdk_sesv2.types.import_destination_type.deserialize_json(
                data["ImportDestinationType"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    return out
