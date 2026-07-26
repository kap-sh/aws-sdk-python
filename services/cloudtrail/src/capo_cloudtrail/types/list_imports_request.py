"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListImportsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.event_data_store_arn
    import capo_cloudtrail.types.import_status
    import capo_cloudtrail.types.list_imports_max_results_count
    import capo_cloudtrail.types.pagination_token


class ListImportsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_cloudtrail.types.list_imports_max_results_count.ListImportsMaxResultsCount"
    ]
    """<p> The maximum number of imports to display on a single page. </p>"""
    destination: NotRequired[
        "capo_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    ]
    """<p> The ARN of the destination event data store. </p>"""
    import_status: NotRequired["capo_cloudtrail.types.import_status.ImportStatus"]
    """<p> The status of the import. </p>"""
    next_token: NotRequired["capo_cloudtrail.types.pagination_token.PaginationToken"]
    """<p> A token you can use to get the next page of import results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListImportsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "destination" in value:
        out["Destination"] = value["destination"]
    if "import_status" in value:
        import capo_cloudtrail.types.import_status

        out["ImportStatus"] = (
            capo_cloudtrail.types.import_status.serialize_aws_json_1_1(
                value["import_status"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListImportsRequest:
    out: ListImportsRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "Destination" in data:
        out["destination"] = data["Destination"]
    if "ImportStatus" in data:
        import capo_cloudtrail.types.import_status

        out["import_status"] = (
            capo_cloudtrail.types.import_status.deserialize_aws_json_1_1(
                data["ImportStatus"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
