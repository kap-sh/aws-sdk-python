"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListResourceSnapshotJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.engagement_identifier
    import aws_sdk_partnercentral_selling.types.page_size
    import aws_sdk_partnercentral_selling.types.resource_snapshot_job_status
    import aws_sdk_partnercentral_selling.types.sort_object


class ListResourceSnapshotJobsRequest(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p> Specifies the catalog related to the request. </p>"""
    max_results: "aws_sdk_partnercentral_selling.types.page_size.PageSize"
    """<p> The maximum number of results to return in a single call. If omitted, defaults to 50. </p>"""
    next_token: NotRequired["str"]
    """<p> The token for the next set of results. </p>"""
    engagement_identifier: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    ]
    """<p> The identifier of the engagement to filter the response. </p>"""
    status: NotRequired[
        "aws_sdk_partnercentral_selling.types.resource_snapshot_job_status.ResourceSnapshotJobStatus"
    ]
    """<p> The status of the jobs to filter the response. </p>"""
    sort: NotRequired["aws_sdk_partnercentral_selling.types.sort_object.SortObject"]
    """<p> Configures the sorting of the response. If omitted, results are sorted by <code>CreatedDate</code> in descending order. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListResourceSnapshotJobsRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["MaxResults"] = value.get("max_results", 100)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "engagement_identifier" in value:
        out["EngagementIdentifier"] = value["engagement_identifier"]
    if "status" in value:
        import aws_sdk_partnercentral_selling.types.resource_snapshot_job_status

        out["Status"] = (
            aws_sdk_partnercentral_selling.types.resource_snapshot_job_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "sort" in value:
        import aws_sdk_partnercentral_selling.types.sort_object

        out["Sort"] = (
            aws_sdk_partnercentral_selling.types.sort_object.serialize_aws_json_1_0(
                value["sort"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListResourceSnapshotJobsRequest:
    out: ListResourceSnapshotJobsRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("ListResourceSnapshotJobsRequest.catalog required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 100
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "EngagementIdentifier" in data:
        out["engagement_identifier"] = data["EngagementIdentifier"]
    if "Status" in data:
        import aws_sdk_partnercentral_selling.types.resource_snapshot_job_status

        out["status"] = (
            aws_sdk_partnercentral_selling.types.resource_snapshot_job_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "Sort" in data:
        import aws_sdk_partnercentral_selling.types.sort_object

        out["sort"] = (
            aws_sdk_partnercentral_selling.types.sort_object.deserialize_aws_json_1_0(
                data["Sort"]
            )
        )
    return out
