"""Generated from Smithy shape ``com.amazonaws.forecast#WhatIfForecastExportSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.data_destination
    import capo_forecast.types.error_message
    import capo_forecast.types.long_arn
    import capo_forecast.types.name
    import capo_forecast.types.status
    import capo_forecast.types.timestamp
    import capo_forecast.types.what_if_forecast_arn_list_for_export


class WhatIfForecastExportSummary(TypedDict, closed=True):
    what_if_forecast_export_arn: NotRequired["capo_forecast.types.long_arn.LongArn"]
    """<p>The Amazon Resource Name (ARN) of the what-if forecast export.</p>"""
    what_if_forecast_arns: NotRequired[
        "capo_forecast.types.what_if_forecast_arn_list_for_export.WhatIfForecastArnListForExport"
    ]
    """<p>An array of Amazon Resource Names (ARNs) that define the what-if forecasts included in the export.</p>"""
    what_if_forecast_export_name: NotRequired["capo_forecast.types.name.Name"]
    """<p>The what-if forecast export name.</p>"""
    destination: NotRequired["capo_forecast.types.data_destination.DataDestination"]
    """<p>The path to the Amazon Simple Storage Service (Amazon S3) bucket where the forecast is exported.</p>"""
    status: NotRequired["capo_forecast.types.status.Status"]
    """<p>The status of the what-if forecast export. States include:</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>CREATE_STOPPING</code>, <code>CREATE_STOPPED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> </ul> <note> <p>The <code>Status</code> of the what-if analysis must be <code>ACTIVE</code> before you can access the analysis.</p> </note>"""
    message: NotRequired["capo_forecast.types.error_message.ErrorMessage"]
    """<p>If an error occurred, an informational message about the error.</p>"""
    creation_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>When the what-if forecast export was created.</p>"""
    last_modification_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>The last time the resource was modified. The timestamp depends on the status of the job:</p> <ul> <li> <p> <code>CREATE_PENDING</code> - The <code>CreationTime</code>.</p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPING</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPED</code> - When the job stopped.</p> </li> <li> <p> <code>ACTIVE</code> or <code>CREATE_FAILED</code> - When the job finished or failed.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WhatIfForecastExportSummary) -> dict:
    out: dict = {}
    if "what_if_forecast_export_arn" in value:
        out["WhatIfForecastExportArn"] = value["what_if_forecast_export_arn"]
    if "what_if_forecast_arns" in value:
        import capo_forecast.types.what_if_forecast_arn_list_for_export

        out["WhatIfForecastArns"] = (
            capo_forecast.types.what_if_forecast_arn_list_for_export.serialize_aws_json_1_1(
                value["what_if_forecast_arns"]
            )
        )
    if "what_if_forecast_export_name" in value:
        out["WhatIfForecastExportName"] = value["what_if_forecast_export_name"]
    if "destination" in value:
        import capo_forecast.types.data_destination

        out["Destination"] = (
            capo_forecast.types.data_destination.serialize_aws_json_1_1(
                value["destination"]
            )
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "message" in value:
        out["Message"] = value["message"]
    if "creation_time" in value:
        import capo_forecast.types.timestamp

        out["CreationTime"] = capo_forecast.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modification_time" in value:
        import capo_forecast.types.timestamp

        out["LastModificationTime"] = (
            capo_forecast.types.timestamp.serialize_aws_json_1_1(
                value["last_modification_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WhatIfForecastExportSummary:
    out: WhatIfForecastExportSummary = {}  # type: ignore[typeddict-item]
    if "WhatIfForecastExportArn" in data:
        out["what_if_forecast_export_arn"] = data["WhatIfForecastExportArn"]
    if "WhatIfForecastArns" in data:
        import capo_forecast.types.what_if_forecast_arn_list_for_export

        out["what_if_forecast_arns"] = (
            capo_forecast.types.what_if_forecast_arn_list_for_export.deserialize_aws_json_1_1(
                data["WhatIfForecastArns"]
            )
        )
    if "WhatIfForecastExportName" in data:
        out["what_if_forecast_export_name"] = data["WhatIfForecastExportName"]
    if "Destination" in data:
        import capo_forecast.types.data_destination

        out["destination"] = (
            capo_forecast.types.data_destination.deserialize_aws_json_1_1(
                data["Destination"]
            )
        )
    if "Status" in data:
        out["status"] = data["Status"]
    if "Message" in data:
        out["message"] = data["Message"]
    if "CreationTime" in data:
        import capo_forecast.types.timestamp

        out["creation_time"] = capo_forecast.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastModificationTime" in data:
        import capo_forecast.types.timestamp

        out["last_modification_time"] = (
            capo_forecast.types.timestamp.deserialize_aws_json_1_1(
                data["LastModificationTime"]
            )
        )
    return out
