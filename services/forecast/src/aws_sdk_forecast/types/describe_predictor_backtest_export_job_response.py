"""Generated from Smithy shape ``com.amazonaws.forecast#DescribePredictorBacktestExportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn
    import aws_sdk_forecast.types.data_destination
    import aws_sdk_forecast.types.format
    import aws_sdk_forecast.types.message
    import aws_sdk_forecast.types.name
    import aws_sdk_forecast.types.status
    import aws_sdk_forecast.types.timestamp


class DescribePredictorBacktestExportJobResponse(TypedDict, closed=True):
    predictor_backtest_export_job_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the predictor backtest export job.</p>"""
    predictor_backtest_export_job_name: NotRequired["aws_sdk_forecast.types.name.Name"]
    """<p>The name of the predictor backtest export job.</p>"""
    predictor_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the predictor.</p>"""
    destination: NotRequired["aws_sdk_forecast.types.data_destination.DataDestination"]
    message: NotRequired["aws_sdk_forecast.types.message.Message"]
    """<p>Information about any errors that may have occurred during the backtest export.</p>"""
    status: NotRequired["aws_sdk_forecast.types.status.Status"]
    """<p>The status of the predictor backtest export job. States include: </p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>CREATE_STOPPING</code>, <code>CREATE_STOPPED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> </ul>"""
    creation_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>When the predictor backtest export job was created.</p>"""
    last_modification_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>The last time the resource was modified. The timestamp depends on the status of the job:</p> <ul> <li> <p> <code>CREATE_PENDING</code> - The <code>CreationTime</code>.</p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPING</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPED</code> - When the job stopped.</p> </li> <li> <p> <code>ACTIVE</code> or <code>CREATE_FAILED</code> - When the job finished or failed.</p> </li> </ul>"""
    format: NotRequired["aws_sdk_forecast.types.format.Format"]
    """<p>The format of the exported data, CSV or PARQUET.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePredictorBacktestExportJobResponse) -> dict:
    out: dict = {}
    if "predictor_backtest_export_job_arn" in value:
        out["PredictorBacktestExportJobArn"] = value[
            "predictor_backtest_export_job_arn"
        ]
    if "predictor_backtest_export_job_name" in value:
        out["PredictorBacktestExportJobName"] = value[
            "predictor_backtest_export_job_name"
        ]
    if "predictor_arn" in value:
        out["PredictorArn"] = value["predictor_arn"]
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


def deserialize_aws_json_1_1(data: dict) -> DescribePredictorBacktestExportJobResponse:
    out: DescribePredictorBacktestExportJobResponse = {}  # type: ignore[typeddict-item]
    if "PredictorBacktestExportJobArn" in data:
        out["predictor_backtest_export_job_arn"] = data["PredictorBacktestExportJobArn"]
    if "PredictorBacktestExportJobName" in data:
        out["predictor_backtest_export_job_name"] = data[
            "PredictorBacktestExportJobName"
        ]
    if "PredictorArn" in data:
        out["predictor_arn"] = data["PredictorArn"]
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
