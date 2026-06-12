"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListMlflowTrackingServersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.mlflow_version
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.sort_order
    import aws_sdk_sagemaker.types.sort_tracking_server_by
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.tracking_server_status


class ListMlflowTrackingServersRequest(TypedDict):
    created_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Use the <code>CreatedAfter</code> filter to only list tracking servers created after a specific date and time. Listed tracking servers are shown with a date and time such as <code>\"2024-03-16T01:46:56+00:00\"</code>. The <code>CreatedAfter</code> parameter takes in a Unix timestamp. To convert a date and time into a Unix timestamp, see <a href=\"https://www.epochconverter.com/\">EpochConverter</a>.</p>"""
    created_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Use the <code>CreatedBefore</code> filter to only list tracking servers created before a specific date and time. Listed tracking servers are shown with a date and time such as <code>\"2024-03-16T01:46:56+00:00\"</code>. The <code>CreatedBefore</code> parameter takes in a Unix timestamp. To convert a date and time into a Unix timestamp, see <a href=\"https://www.epochconverter.com/\">EpochConverter</a>.</p>"""
    tracking_server_status: NotRequired[
        "aws_sdk_sagemaker.types.tracking_server_status.TrackingServerStatus"
    ]
    """<p>Filter for tracking servers with a specified creation status.</p>"""
    mlflow_version: NotRequired["aws_sdk_sagemaker.types.mlflow_version.MlflowVersion"]
    """<p>Filter for tracking servers using the specified MLflow version.</p>"""
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.sort_tracking_server_by.SortTrackingServerBy"
    ]
    """<p>Filter for trackings servers sorting by name, creation time, or creation status.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.sort_order.SortOrder"]
    """<p>Change the order of the listed tracking servers. By default, tracking servers are listed in <code>Descending</code> order by creation time. To change the list order, you can specify <code>SortOrder</code> to be <code>Ascending</code>.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of tracking servers to list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMlflowTrackingServersRequest) -> dict:
    out: dict = {}
    if "created_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreatedAfter"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_after"]
        )
    if "created_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreatedBefore"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_before"]
        )
    if "tracking_server_status" in value:
        import aws_sdk_sagemaker.types.tracking_server_status

        out["TrackingServerStatus"] = (
            aws_sdk_sagemaker.types.tracking_server_status.serialize_aws_json_1_1(
                value["tracking_server_status"]
            )
        )
    if "mlflow_version" in value:
        out["MlflowVersion"] = value["mlflow_version"]
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.sort_tracking_server_by

        out["SortBy"] = (
            aws_sdk_sagemaker.types.sort_tracking_server_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.sort_order

        out["SortOrder"] = aws_sdk_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMlflowTrackingServersRequest:
    out: ListMlflowTrackingServersRequest = {}  # type: ignore[typeddict-item]
    if "CreatedAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["created_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreatedAfter"]
            )
        )
    if "CreatedBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["created_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreatedBefore"]
            )
        )
    if "TrackingServerStatus" in data:
        import aws_sdk_sagemaker.types.tracking_server_status

        out["tracking_server_status"] = (
            aws_sdk_sagemaker.types.tracking_server_status.deserialize_aws_json_1_1(
                data["TrackingServerStatus"]
            )
        )
    if "MlflowVersion" in data:
        out["mlflow_version"] = data["MlflowVersion"]
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.sort_tracking_server_by

        out["sort_by"] = (
            aws_sdk_sagemaker.types.sort_tracking_server_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.sort_order

        out["sort_order"] = aws_sdk_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
