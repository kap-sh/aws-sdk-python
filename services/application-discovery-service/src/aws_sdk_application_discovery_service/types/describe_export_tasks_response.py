"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DescribeExportTasksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.exports_info
    import aws_sdk_application_discovery_service.types.next_token


class DescribeExportTasksResponse(TypedDict, closed=True):
    exports_info: NotRequired[
        "aws_sdk_application_discovery_service.types.exports_info.ExportsInfo"
    ]
    """<p>Contains one or more sets of export request details. When the status of a request is <code>SUCCEEDED</code>, the response includes a URL for an Amazon S3 bucket where you can view the data in a CSV file.</p>"""
    next_token: NotRequired[
        "aws_sdk_application_discovery_service.types.next_token.NextToken"
    ]
    """<p>The <code>nextToken</code> value to include in a future <code>DescribeExportTasks</code> request. When the results of a <code>DescribeExportTasks</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeExportTasksResponse) -> dict:
    out: dict = {}
    if "exports_info" in value:
        import aws_sdk_application_discovery_service.types.exports_info

        out["exportsInfo"] = (
            aws_sdk_application_discovery_service.types.exports_info.serialize_aws_json_1_1(
                value["exports_info"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeExportTasksResponse:
    out: DescribeExportTasksResponse = {}  # type: ignore[typeddict-item]
    if "exportsInfo" in data:
        import aws_sdk_application_discovery_service.types.exports_info

        out["exports_info"] = (
            aws_sdk_application_discovery_service.types.exports_info.deserialize_aws_json_1_1(
                data["exportsInfo"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
