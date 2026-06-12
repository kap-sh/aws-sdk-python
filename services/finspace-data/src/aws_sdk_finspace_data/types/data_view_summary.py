"""Generated from Smithy shape ``com.amazonaws.finspacedata#DataViewSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.boolean
    import aws_sdk_finspace_data.types.data_view_arn
    import aws_sdk_finspace_data.types.data_view_destination_type_params
    import aws_sdk_finspace_data.types.data_view_error_info
    import aws_sdk_finspace_data.types.data_view_id
    import aws_sdk_finspace_data.types.data_view_status
    import aws_sdk_finspace_data.types.dataset_id
    import aws_sdk_finspace_data.types.partition_column_list
    import aws_sdk_finspace_data.types.sort_column_list
    import aws_sdk_finspace_data.types.timestamp_epoch


class DataViewSummary(TypedDict):
    data_view_id: NotRequired["aws_sdk_finspace_data.types.data_view_id.DataViewId"]
    """<p>The unique identifier for the Dataview.</p>"""
    data_view_arn: NotRequired["aws_sdk_finspace_data.types.data_view_arn.DataViewArn"]
    """<p>The ARN identifier of the Dataview.</p>"""
    dataset_id: NotRequired["aws_sdk_finspace_data.types.dataset_id.DatasetId"]
    """<p>Th unique identifier for the Dataview Dataset.</p>"""
    as_of_timestamp: NotRequired[
        "aws_sdk_finspace_data.types.timestamp_epoch.TimestampEpoch"
    ]
    """<p>Time range to use for the Dataview. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    partition_columns: NotRequired[
        "aws_sdk_finspace_data.types.partition_column_list.PartitionColumnList"
    ]
    """<p>Ordered set of column names used to partition data.</p>"""
    sort_columns: NotRequired[
        "aws_sdk_finspace_data.types.sort_column_list.SortColumnList"
    ]
    """<p>Columns to be used for sorting the data.</p>"""
    status: NotRequired["aws_sdk_finspace_data.types.data_view_status.DataViewStatus"]
    """<p>The status of a Dataview creation.</p> <ul> <li> <p> <code>RUNNING</code> – Dataview creation is running.</p> </li> <li> <p> <code>STARTING</code> – Dataview creation is starting.</p> </li> <li> <p> <code>FAILED</code> – Dataview creation has failed.</p> </li> <li> <p> <code>CANCELLED</code> – Dataview creation has been cancelled.</p> </li> <li> <p> <code>TIMEOUT</code> – Dataview creation has timed out.</p> </li> <li> <p> <code>SUCCESS</code> – Dataview creation has succeeded.</p> </li> <li> <p> <code>PENDING</code> – Dataview creation is pending.</p> </li> <li> <p> <code>FAILED_CLEANUP_FAILED</code> – Dataview creation failed and resource cleanup failed.</p> </li> </ul>"""
    error_info: NotRequired[
        "aws_sdk_finspace_data.types.data_view_error_info.DataViewErrorInfo"
    ]
    """<p>The structure with error messages.</p>"""
    destination_type_properties: NotRequired[
        "aws_sdk_finspace_data.types.data_view_destination_type_params.DataViewDestinationTypeParams"
    ]
    """<p>Information about the Dataview destination.</p>"""
    auto_update: "aws_sdk_finspace_data.types.boolean.Boolean"
    """<p>The flag to indicate Dataview should be updated automatically.</p>"""
    create_time: "aws_sdk_finspace_data.types.timestamp_epoch.TimestampEpoch"
    """<p>The timestamp at which the Dataview was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    last_modified_time: "aws_sdk_finspace_data.types.timestamp_epoch.TimestampEpoch"
    """<p>The last time that a Dataview was modified. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataViewSummary) -> dict:
    out: dict = {}
    if "data_view_id" in value:
        out["dataViewId"] = value["data_view_id"]
    if "data_view_arn" in value:
        out["dataViewArn"] = value["data_view_arn"]
    if "dataset_id" in value:
        out["datasetId"] = value["dataset_id"]
    if "as_of_timestamp" in value:
        out["asOfTimestamp"] = value["as_of_timestamp"]
    if "partition_columns" in value:
        import aws_sdk_finspace_data.types.partition_column_list

        out["partitionColumns"] = (
            aws_sdk_finspace_data.types.partition_column_list.serialize_json(
                value["partition_columns"]
            )
        )
    if "sort_columns" in value:
        import aws_sdk_finspace_data.types.sort_column_list

        out["sortColumns"] = (
            aws_sdk_finspace_data.types.sort_column_list.serialize_json(
                value["sort_columns"]
            )
        )
    if "status" in value:
        import aws_sdk_finspace_data.types.data_view_status

        out["status"] = aws_sdk_finspace_data.types.data_view_status.serialize_json(
            value["status"]
        )
    if "error_info" in value:
        import aws_sdk_finspace_data.types.data_view_error_info

        out["errorInfo"] = (
            aws_sdk_finspace_data.types.data_view_error_info.serialize_json(
                value["error_info"]
            )
        )
    if "destination_type_properties" in value:
        import aws_sdk_finspace_data.types.data_view_destination_type_params

        out["destinationTypeProperties"] = (
            aws_sdk_finspace_data.types.data_view_destination_type_params.serialize_json(
                value["destination_type_properties"]
            )
        )
    out["autoUpdate"] = value.get("auto_update", False)
    out["createTime"] = value.get("create_time", 0)
    out["lastModifiedTime"] = value.get("last_modified_time", 0)
    return out


def deserialize_json(data: dict) -> DataViewSummary:
    out: DataViewSummary = {}  # type: ignore[typeddict-item]
    if "dataViewId" in data:
        out["data_view_id"] = data["dataViewId"]
    if "dataViewArn" in data:
        out["data_view_arn"] = data["dataViewArn"]
    if "datasetId" in data:
        out["dataset_id"] = data["datasetId"]
    if "asOfTimestamp" in data:
        out["as_of_timestamp"] = data["asOfTimestamp"]
    if "partitionColumns" in data:
        import aws_sdk_finspace_data.types.partition_column_list

        out["partition_columns"] = (
            aws_sdk_finspace_data.types.partition_column_list.deserialize_json(
                data["partitionColumns"]
            )
        )
    if "sortColumns" in data:
        import aws_sdk_finspace_data.types.sort_column_list

        out["sort_columns"] = (
            aws_sdk_finspace_data.types.sort_column_list.deserialize_json(
                data["sortColumns"]
            )
        )
    if "status" in data:
        import aws_sdk_finspace_data.types.data_view_status

        out["status"] = aws_sdk_finspace_data.types.data_view_status.deserialize_json(
            data["status"]
        )
    if "errorInfo" in data:
        import aws_sdk_finspace_data.types.data_view_error_info

        out["error_info"] = (
            aws_sdk_finspace_data.types.data_view_error_info.deserialize_json(
                data["errorInfo"]
            )
        )
    if "destinationTypeProperties" in data:
        import aws_sdk_finspace_data.types.data_view_destination_type_params

        out["destination_type_properties"] = (
            aws_sdk_finspace_data.types.data_view_destination_type_params.deserialize_json(
                data["destinationTypeProperties"]
            )
        )
    if "autoUpdate" in data:
        out["auto_update"] = data["autoUpdate"]
    else:
        out["auto_update"] = False
    if "createTime" in data:
        out["create_time"] = data["createTime"]
    else:
        out["create_time"] = 0
    if "lastModifiedTime" in data:
        out["last_modified_time"] = data["lastModifiedTime"]
    else:
        out["last_modified_time"] = 0
    return out
