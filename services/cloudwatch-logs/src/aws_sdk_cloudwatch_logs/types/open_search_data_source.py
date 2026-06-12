"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OpenSearchDataSource``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.open_search_data_source_name
    import aws_sdk_cloudwatch_logs.types.open_search_resource_status


class OpenSearchDataSource(TypedDict):
    data_source_name: NotRequired[
        "aws_sdk_cloudwatch_logs.types.open_search_data_source_name.OpenSearchDataSourceName"
    ]
    """<p>The name of the OpenSearch Service data source.</p>"""
    status: NotRequired[
        "aws_sdk_cloudwatch_logs.types.open_search_resource_status.OpenSearchResourceStatus"
    ]
    """<p>This structure contains information about the status of this OpenSearch Service resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenSearchDataSource) -> dict:
    out: dict = {}
    if "data_source_name" in value:
        out["dataSourceName"] = value["data_source_name"]
    if "status" in value:
        import aws_sdk_cloudwatch_logs.types.open_search_resource_status

        out["status"] = (
            aws_sdk_cloudwatch_logs.types.open_search_resource_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenSearchDataSource:
    out: OpenSearchDataSource = {}  # type: ignore[typeddict-item]
    if "dataSourceName" in data:
        out["data_source_name"] = data["dataSourceName"]
    if "status" in data:
        import aws_sdk_cloudwatch_logs.types.open_search_resource_status

        out["status"] = (
            aws_sdk_cloudwatch_logs.types.open_search_resource_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out
