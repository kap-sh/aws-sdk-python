"""Generated from Smithy shape ``com.amazonaws.forecast#DescribeForecastExportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.data_destination
    import capo_forecast.types.format
    import capo_forecast.types.message
    import capo_forecast.types.name
    import capo_forecast.types.status
    import capo_forecast.types.timestamp


class DescribeForecastExportJobResponse(TypedDict, closed=True):
    forecast_export_job_arn: NotRequired["capo_forecast.types.arn.Arn"]
    """<p>The ARN of the forecast export job.</p>"""
    forecast_export_job_name: NotRequired["capo_forecast.types.name.Name"]
    """<p>The name of the forecast export job.</p>"""
    forecast_arn: NotRequired["capo_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the exported forecast.</p>"""
    destination: NotRequired["capo_forecast.types.data_destination.DataDestination"]
    """<p>The path to the Amazon Simple Storage Service (Amazon S3) bucket where the forecast is exported.</p>"""
    message: NotRequired["capo_forecast.types.message.Message"]
    """<p>If an error occurred, an informational message about the error.</p>"""
    status: NotRequired["capo_forecast.types.status.Status"]
    """<p>The status of the forecast export job. States include:</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>CREATE_STOPPING</code>, <code>CREATE_STOPPED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> </ul> <note> <p>The <code>Status</code> of the forecast export job must be <code>ACTIVE</code> before you can access the forecast in your S3 bucket.</p> </note>"""
    creation_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>When the forecast export job was created.</p>"""
    last_modification_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>The last time the resource was modified. The timestamp depends on the status of the job:</p> <ul> <li> <p> <code>CREATE_PENDING</code> - The <code>CreationTime</code>.</p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPING</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPED</code> - When the job stopped.</p> </li> <li> <p> <code>ACTIVE</code> or <code>CREATE_FAILED</code> - When the job finished or failed.</p> </li> </ul>"""
    format: NotRequired["capo_forecast.types.format.Format"]
    """<p>The format of the exported data, CSV or PARQUET.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeForecastExportJobResponse) -> dict:
    out: dict = {}
    if "forecast_export_job_arn" in value:
        out["ForecastExportJobArn"] = value["forecast_export_job_arn"]
    if "forecast_export_job_name" in value:
        out["ForecastExportJobName"] = value["forecast_export_job_name"]
    if "forecast_arn" in value:
        out["ForecastArn"] = value["forecast_arn"]
    if "destination" in value:
        import capo_forecast.types.data_destination

        out["Destination"] = (
            capo_forecast.types.data_destination.serialize_aws_json_1_1(
                value["destination"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "status" in value:
        out["Status"] = value["status"]
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
    if "format" in value:
        out["Format"] = value["format"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeForecastExportJobResponse:
    out: DescribeForecastExportJobResponse = {}  # type: ignore[typeddict-item]
    if "ForecastExportJobArn" in data:
        out["forecast_export_job_arn"] = data["ForecastExportJobArn"]
    if "ForecastExportJobName" in data:
        out["forecast_export_job_name"] = data["ForecastExportJobName"]
    if "ForecastArn" in data:
        out["forecast_arn"] = data["ForecastArn"]
    if "Destination" in data:
        import capo_forecast.types.data_destination

        out["destination"] = (
            capo_forecast.types.data_destination.deserialize_aws_json_1_1(
                data["Destination"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "Status" in data:
        out["status"] = data["Status"]
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
    if "Format" in data:
        out["format"] = data["Format"]
    return out
