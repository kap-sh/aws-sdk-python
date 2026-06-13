"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListTableRestoreStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.pagination_token


class ListTableRestoreStatusRequest(TypedDict):
    next_token: NotRequired[
        "aws_sdk_redshift_serverless.types.pagination_token.PaginationToken"
    ]
    """<p>If your initial <code>ListTableRestoreStatus</code> operation returns a nextToken, you can include the returned <code>nextToken</code> in following <code>ListTableRestoreStatus</code> operations. This will return results on the next page.</p>"""
    max_results: NotRequired["int"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use nextToken to display the next page of results.</p>"""
    namespace_name: NotRequired["str"]
    """<p>The namespace from which to list all of the statuses of <code>RestoreTableFromSnapshot</code> operations .</p>"""
    workgroup_name: NotRequired["str"]
    """<p>The workgroup from which to list all of the statuses of <code>RestoreTableFromSnapshot</code> operations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTableRestoreStatusRequest) -> dict:
    out: dict = {}
    if "namespace_name" in value:
        out["namespaceName"] = value["namespace_name"]
    if "workgroup_name" in value:
        out["workgroupName"] = value["workgroup_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTableRestoreStatusRequest:
    out: ListTableRestoreStatusRequest = {}  # type: ignore[typeddict-item]
    if "namespaceName" in data:
        out["namespace_name"] = data["namespaceName"]
    if "workgroupName" in data:
        out["workgroup_name"] = data["workgroupName"]
    return out
