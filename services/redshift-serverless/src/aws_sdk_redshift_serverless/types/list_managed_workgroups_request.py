"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListManagedWorkgroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.pagination_token
    import aws_sdk_redshift_serverless.types.source_arn


class ListManagedWorkgroupsRequest(TypedDict, closed=True):
    source_arn: NotRequired["aws_sdk_redshift_serverless.types.source_arn.SourceArn"]
    """<p>The Amazon Resource Name (ARN) for the managed workgroup in the Glue Data Catalog.</p>"""
    next_token: NotRequired[
        "aws_sdk_redshift_serverless.types.pagination_token.PaginationToken"
    ]
    """<p>If your initial ListManagedWorkgroups operation returns a nextToken, you can include the returned nextToken in following ListManagedWorkgroups operations, which returns results in the next page.</p>"""
    max_results: NotRequired["int"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use nextToken to display the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListManagedWorkgroupsRequest) -> dict:
    out: dict = {}
    if "source_arn" in value:
        out["sourceArn"] = value["source_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListManagedWorkgroupsRequest:
    out: ListManagedWorkgroupsRequest = {}  # type: ignore[typeddict-item]
    if "sourceArn" in data:
        out["source_arn"] = data["sourceArn"]
    return out
