"""Generated from Smithy shape ``com.amazonaws.forecast#DescribeWhatIfForecastExportResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.data_destination
    import aws_sdk_forecast.types.format
    import aws_sdk_forecast.types.long
    import aws_sdk_forecast.types.long_arn
    import aws_sdk_forecast.types.long_arn_list
    import aws_sdk_forecast.types.message
    import aws_sdk_forecast.types.name
    import aws_sdk_forecast.types.status
    import aws_sdk_forecast.types.timestamp


class DescribeWhatIfForecastExportResponse(TypedDict):
    what_if_forecast_export_arn: NotRequired["aws_sdk_forecast.types.long_arn.LongArn"]
    """<p>The Amazon Resource Name (ARN) of the what-if forecast export.</p>"""
    what_if_forecast_export_name: NotRequired["aws_sdk_forecast.types.name.Name"]
    """<p>The name of the what-if forecast export.</p>"""
    what_if_forecast_arns: NotRequired[
        "aws_sdk_forecast.types.long_arn_list.LongArnList"
    ]
    """<p>An array of Amazon Resource Names (ARNs) that represent all of the what-if forecasts exported in this resource.</p>"""
    destination: NotRequired["aws_sdk_forecast.types.data_destination.DataDestination"]
    message: NotRequired["aws_sdk_forecast.types.message.Message"]
    """<p>If an error occurred, an informational message about the error.</p>"""
    status: NotRequired["aws_sdk_forecast.types.status.Status"]
    """<p>The status of the what-if forecast. States include:</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>CREATE_STOPPING</code>, <code>CREATE_STOPPED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> </ul> <note> <p>The <code>Status</code> of the what-if forecast export must be <code>ACTIVE</code> before you can access the forecast export.</p> </note>"""
    creation_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>When the what-if forecast export was created.</p>"""
    estimated_time_remaining_in_minutes: NotRequired["aws_sdk_forecast.types.long.Long"]
    """<p>The approximate time remaining to complete the what-if forecast export, in minutes.</p>"""
    last_modification_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>The last time the resource was modified. The timestamp depends on the status of the job:</p> <ul> <li> <p> <code>CREATE_PENDING</code> - The <code>CreationTime</code>.</p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPING</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPED</code> - When the job stopped.</p> </li> <li> <p> <code>ACTIVE</code> or <code>CREATE_FAILED</code> - When the job finished or failed.</p> </li> </ul>"""
    format: NotRequired["aws_sdk_forecast.types.format.Format"]
    """<p>The format of the exported data, CSV or PARQUET.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWhatIfForecastExportResponse) -> dict:
    out: dict = {}
    if "what_if_forecast_export_arn" in value:
        out["WhatIfForecastExportArn"] = value["what_if_forecast_export_arn"]
    if "what_if_forecast_export_name" in value:
        out["WhatIfForecastExportName"] = value["what_if_forecast_export_name"]
    if "what_if_forecast_arns" in value:
        import aws_sdk_forecast.types.long_arn_list

        out["WhatIfForecastArns"] = (
            aws_sdk_forecast.types.long_arn_list.serialize_aws_json_1_1(
                value["what_if_forecast_arns"]
            )
        )
    if "destination" in value:
        import aws_sdk_forecast.types.data_destination

        out["Destination"] = (
            aws_sdk_forecast.types.data_destination.serialize_aws_json_1_1(
                value["destination"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "status" in value:
        out["Status"] = value["status"]
    if "creation_time" in value:
        import aws_sdk_forecast.types.timestamp

        out["CreationTime"] = aws_sdk_forecast.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "estimated_time_remaining_in_minutes" in value:
        out["EstimatedTimeRemainingInMinutes"] = value[
            "estimated_time_remaining_in_minutes"
        ]
    if "last_modification_time" in value:
        import aws_sdk_forecast.types.timestamp

        out["LastModificationTime"] = (
            aws_sdk_forecast.types.timestamp.serialize_aws_json_1_1(
                value["last_modification_time"]
            )
        )
    if "format" in value:
        out["Format"] = value["format"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWhatIfForecastExportResponse:
    out: DescribeWhatIfForecastExportResponse = {}  # type: ignore[typeddict-item]
    if "WhatIfForecastExportArn" in data:
        out["what_if_forecast_export_arn"] = data["WhatIfForecastExportArn"]
    if "WhatIfForecastExportName" in data:
        out["what_if_forecast_export_name"] = data["WhatIfForecastExportName"]
    if "WhatIfForecastArns" in data:
        import aws_sdk_forecast.types.long_arn_list

        out["what_if_forecast_arns"] = (
            aws_sdk_forecast.types.long_arn_list.deserialize_aws_json_1_1(
                data["WhatIfForecastArns"]
            )
        )
    if "Destination" in data:
        import aws_sdk_forecast.types.data_destination

        out["destination"] = (
            aws_sdk_forecast.types.data_destination.deserialize_aws_json_1_1(
                data["Destination"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "CreationTime" in data:
        import aws_sdk_forecast.types.timestamp

        out["creation_time"] = (
            aws_sdk_forecast.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "EstimatedTimeRemainingInMinutes" in data:
        out["estimated_time_remaining_in_minutes"] = data[
            "EstimatedTimeRemainingInMinutes"
        ]
    if "LastModificationTime" in data:
        import aws_sdk_forecast.types.timestamp

        out["last_modification_time"] = (
            aws_sdk_forecast.types.timestamp.deserialize_aws_json_1_1(
                data["LastModificationTime"]
            )
        )
    if "Format" in data:
        out["format"] = data["Format"]
    return out
