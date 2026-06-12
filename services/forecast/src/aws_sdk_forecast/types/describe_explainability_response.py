"""Generated from Smithy shape ``com.amazonaws.forecast#DescribeExplainabilityResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn
    import aws_sdk_forecast.types.boolean
    import aws_sdk_forecast.types.data_source
    import aws_sdk_forecast.types.explainability_config
    import aws_sdk_forecast.types.local_date_time
    import aws_sdk_forecast.types.long
    import aws_sdk_forecast.types.message
    import aws_sdk_forecast.types.name
    import aws_sdk_forecast.types.schema
    import aws_sdk_forecast.types.status
    import aws_sdk_forecast.types.timestamp


class DescribeExplainabilityResponse(TypedDict):
    explainability_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the Explainability.</p>"""
    explainability_name: NotRequired["aws_sdk_forecast.types.name.Name"]
    """<p>The name of the Explainability.</p>"""
    resource_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the Predictor or Forecast used to create the Explainability resource.</p>"""
    explainability_config: NotRequired[
        "aws_sdk_forecast.types.explainability_config.ExplainabilityConfig"
    ]
    """<p>The configuration settings that define the granularity of time series and time points for the Explainability.</p>"""
    enable_visualization: NotRequired["aws_sdk_forecast.types.boolean.Boolean"]
    """<p>Whether the visualization was enabled for the Explainability resource.</p>"""
    data_source: NotRequired["aws_sdk_forecast.types.data_source.DataSource"]
    schema: NotRequired["aws_sdk_forecast.types.schema.Schema"]
    start_date_time: NotRequired["aws_sdk_forecast.types.local_date_time.LocalDateTime"]
    """<p>If <code>TimePointGranularity</code> is set to <code>SPECIFIC</code>, the first time point in the Explainability.</p>"""
    end_date_time: NotRequired["aws_sdk_forecast.types.local_date_time.LocalDateTime"]
    """<p>If <code>TimePointGranularity</code> is set to <code>SPECIFIC</code>, the last time point in the Explainability.</p>"""
    estimated_time_remaining_in_minutes: NotRequired["aws_sdk_forecast.types.long.Long"]
    """<p>The estimated time remaining in minutes for the <a>CreateExplainability</a> job to complete.</p>"""
    message: NotRequired["aws_sdk_forecast.types.message.Message"]
    """<p>If an error occurred, a message about the error.</p>"""
    status: NotRequired["aws_sdk_forecast.types.status.Status"]
    """<p>The status of the Explainability resource. States include: </p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>CREATE_STOPPING</code>, <code>CREATE_STOPPED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> </ul>"""
    creation_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>When the Explainability resource was created.</p>"""
    last_modification_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>The last time the resource was modified. The timestamp depends on the status of the job:</p> <ul> <li> <p> <code>CREATE_PENDING</code> - The <code>CreationTime</code>.</p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPING</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPED</code> - When the job stopped.</p> </li> <li> <p> <code>ACTIVE</code> or <code>CREATE_FAILED</code> - When the job finished or failed.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeExplainabilityResponse) -> dict:
    out: dict = {}
    if "explainability_arn" in value:
        out["ExplainabilityArn"] = value["explainability_arn"]
    if "explainability_name" in value:
        out["ExplainabilityName"] = value["explainability_name"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "explainability_config" in value:
        import aws_sdk_forecast.types.explainability_config

        out["ExplainabilityConfig"] = (
            aws_sdk_forecast.types.explainability_config.serialize_aws_json_1_1(
                value["explainability_config"]
            )
        )
    if "enable_visualization" in value:
        out["EnableVisualization"] = value["enable_visualization"]
    if "data_source" in value:
        import aws_sdk_forecast.types.data_source

        out["DataSource"] = aws_sdk_forecast.types.data_source.serialize_aws_json_1_1(
            value["data_source"]
        )
    if "schema" in value:
        import aws_sdk_forecast.types.schema

        out["Schema"] = aws_sdk_forecast.types.schema.serialize_aws_json_1_1(
            value["schema"]
        )
    if "start_date_time" in value:
        out["StartDateTime"] = value["start_date_time"]
    if "end_date_time" in value:
        out["EndDateTime"] = value["end_date_time"]
    if "estimated_time_remaining_in_minutes" in value:
        out["EstimatedTimeRemainingInMinutes"] = value[
            "estimated_time_remaining_in_minutes"
        ]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeExplainabilityResponse:
    out: DescribeExplainabilityResponse = {}  # type: ignore[typeddict-item]
    if "ExplainabilityArn" in data:
        out["explainability_arn"] = data["ExplainabilityArn"]
    if "ExplainabilityName" in data:
        out["explainability_name"] = data["ExplainabilityName"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "ExplainabilityConfig" in data:
        import aws_sdk_forecast.types.explainability_config

        out["explainability_config"] = (
            aws_sdk_forecast.types.explainability_config.deserialize_aws_json_1_1(
                data["ExplainabilityConfig"]
            )
        )
    if "EnableVisualization" in data:
        out["enable_visualization"] = data["EnableVisualization"]
    if "DataSource" in data:
        import aws_sdk_forecast.types.data_source

        out["data_source"] = (
            aws_sdk_forecast.types.data_source.deserialize_aws_json_1_1(
                data["DataSource"]
            )
        )
    if "Schema" in data:
        import aws_sdk_forecast.types.schema

        out["schema"] = aws_sdk_forecast.types.schema.deserialize_aws_json_1_1(
            data["Schema"]
        )
    if "StartDateTime" in data:
        out["start_date_time"] = data["StartDateTime"]
    if "EndDateTime" in data:
        out["end_date_time"] = data["EndDateTime"]
    if "EstimatedTimeRemainingInMinutes" in data:
        out["estimated_time_remaining_in_minutes"] = data[
            "EstimatedTimeRemainingInMinutes"
        ]
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
    return out
