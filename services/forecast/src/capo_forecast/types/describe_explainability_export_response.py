"""Generated from Smithy shape ``com.amazonaws.forecast#DescribeExplainabilityExportResponse``."""

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


class DescribeExplainabilityExportResponse(TypedDict, closed=True):
    explainability_export_arn: NotRequired["capo_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the Explainability export.</p>"""
    explainability_export_name: NotRequired["capo_forecast.types.name.Name"]
    """<p>The name of the Explainability export.</p>"""
    explainability_arn: NotRequired["capo_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the Explainability export.</p>"""
    destination: NotRequired["capo_forecast.types.data_destination.DataDestination"]
    message: NotRequired["capo_forecast.types.message.Message"]
    """<p>Information about any errors that occurred during the export.</p>"""
    status: NotRequired["capo_forecast.types.status.Status"]
    """<p>The status of the Explainability export. States include: </p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>CREATE_STOPPING</code>, <code>CREATE_STOPPED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> </ul>"""
    creation_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>When the Explainability export was created.</p>"""
    last_modification_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>The last time the resource was modified. The timestamp depends on the status of the job:</p> <ul> <li> <p> <code>CREATE_PENDING</code> - The <code>CreationTime</code>.</p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPING</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPED</code> - When the job stopped.</p> </li> <li> <p> <code>ACTIVE</code> or <code>CREATE_FAILED</code> - When the job finished or failed.</p> </li> </ul>"""
    format: NotRequired["capo_forecast.types.format.Format"]
    """<p>The format of the exported data, CSV or PARQUET.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeExplainabilityExportResponse) -> dict:
    out: dict = {}
    if "explainability_export_arn" in value:
        out["ExplainabilityExportArn"] = value["explainability_export_arn"]
    if "explainability_export_name" in value:
        out["ExplainabilityExportName"] = value["explainability_export_name"]
    if "explainability_arn" in value:
        out["ExplainabilityArn"] = value["explainability_arn"]
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


def deserialize_aws_json_1_1(data: dict) -> DescribeExplainabilityExportResponse:
    out: DescribeExplainabilityExportResponse = {}  # type: ignore[typeddict-item]
    if "ExplainabilityExportArn" in data:
        out["explainability_export_arn"] = data["ExplainabilityExportArn"]
    if "ExplainabilityExportName" in data:
        out["explainability_export_name"] = data["ExplainabilityExportName"]
    if "ExplainabilityArn" in data:
        out["explainability_arn"] = data["ExplainabilityArn"]
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
