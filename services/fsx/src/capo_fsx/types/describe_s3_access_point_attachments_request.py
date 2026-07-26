"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeS3AccessPointAttachmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.max_results
    import capo_fsx.types.next_token
    import capo_fsx.types.s3_access_point_attachment_names
    import capo_fsx.types.s3_access_point_attachments_filters


class DescribeS3AccessPointAttachmentsRequest(TypedDict, closed=True):
    names: NotRequired[
        "capo_fsx.types.s3_access_point_attachment_names.S3AccessPointAttachmentNames"
    ]
    """<p>The names of the S3 access point attachments whose descriptions you want to retrieve.</p>"""
    filters: NotRequired[
        "capo_fsx.types.s3_access_point_attachments_filters.S3AccessPointAttachmentsFilters"
    ]
    """<p>Enter a filter Name and Values pair to view a select set of S3 access point attachments.</p>"""
    max_results: NotRequired["capo_fsx.types.max_results.MaxResults"]
    next_token: NotRequired["capo_fsx.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeS3AccessPointAttachmentsRequest) -> dict:
    out: dict = {}
    if "names" in value:
        import capo_fsx.types.s3_access_point_attachment_names

        out["Names"] = (
            capo_fsx.types.s3_access_point_attachment_names.serialize_aws_json_1_1(
                value["names"]
            )
        )
    if "filters" in value:
        import capo_fsx.types.s3_access_point_attachments_filters

        out["Filters"] = (
            capo_fsx.types.s3_access_point_attachments_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeS3AccessPointAttachmentsRequest:
    out: DescribeS3AccessPointAttachmentsRequest = {}  # type: ignore[typeddict-item]
    if "Names" in data:
        import capo_fsx.types.s3_access_point_attachment_names

        out["names"] = (
            capo_fsx.types.s3_access_point_attachment_names.deserialize_aws_json_1_1(
                data["Names"]
            )
        )
    if "Filters" in data:
        import capo_fsx.types.s3_access_point_attachments_filters

        out["filters"] = (
            capo_fsx.types.s3_access_point_attachments_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
