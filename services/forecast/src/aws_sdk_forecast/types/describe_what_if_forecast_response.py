"""Generated from Smithy shape ``com.amazonaws.forecast#DescribeWhatIfForecastResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn
    import aws_sdk_forecast.types.error_message
    import aws_sdk_forecast.types.forecast_types
    import aws_sdk_forecast.types.long
    import aws_sdk_forecast.types.long_arn
    import aws_sdk_forecast.types.name
    import aws_sdk_forecast.types.string
    import aws_sdk_forecast.types.time_series_replacements_data_source
    import aws_sdk_forecast.types.time_series_transformations
    import aws_sdk_forecast.types.timestamp


class DescribeWhatIfForecastResponse(TypedDict):
    what_if_forecast_name: NotRequired["aws_sdk_forecast.types.name.Name"]
    """<p>The name of the what-if forecast.</p>"""
    what_if_forecast_arn: NotRequired["aws_sdk_forecast.types.long_arn.LongArn"]
    """<p>The Amazon Resource Name (ARN) of the what-if forecast.</p>"""
    what_if_analysis_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the what-if analysis that contains this forecast.</p>"""
    estimated_time_remaining_in_minutes: NotRequired["aws_sdk_forecast.types.long.Long"]
    """<p>The approximate time remaining to complete the what-if forecast, in minutes.</p>"""
    status: NotRequired["aws_sdk_forecast.types.string.String"]
    """<p>The status of the what-if forecast. States include:</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>CREATE_STOPPING</code>, <code>CREATE_STOPPED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> </ul> <note> <p>The <code>Status</code> of the what-if forecast must be <code>ACTIVE</code> before you can access the forecast.</p> </note>"""
    message: NotRequired["aws_sdk_forecast.types.error_message.ErrorMessage"]
    """<p>If an error occurred, an informational message about the error.</p>"""
    creation_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>When the what-if forecast was created.</p>"""
    last_modification_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>The last time the resource was modified. The timestamp depends on the status of the job:</p> <ul> <li> <p> <code>CREATE_PENDING</code> - The <code>CreationTime</code>.</p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPING</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPED</code> - When the job stopped.</p> </li> <li> <p> <code>ACTIVE</code> or <code>CREATE_FAILED</code> - When the job finished or failed.</p> </li> </ul>"""
    time_series_transformations: NotRequired[
        "aws_sdk_forecast.types.time_series_transformations.TimeSeriesTransformations"
    ]
    """<p>An array of <code>Action</code> and <code>TimeSeriesConditions</code> elements that describe what transformations were applied to which time series.</p>"""
    time_series_replacements_data_source: NotRequired[
        "aws_sdk_forecast.types.time_series_replacements_data_source.TimeSeriesReplacementsDataSource"
    ]
    """<p>An array of <code>S3Config</code>, <code>Schema</code>, and <code>Format</code> elements that describe the replacement time series.</p>"""
    forecast_types: NotRequired["aws_sdk_forecast.types.forecast_types.ForecastTypes"]
    r"""<p>The quantiles at which probabilistic forecasts are generated. You can specify up to five quantiles per what-if forecast in the <a>CreateWhatIfForecast</a> operation. If you didn't specify quantiles, the default values are <code>[\"0.1\", \"0.5\", \"0.9\"]</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWhatIfForecastResponse) -> dict:
    out: dict = {}
    if "what_if_forecast_name" in value:
        out["WhatIfForecastName"] = value["what_if_forecast_name"]
    if "what_if_forecast_arn" in value:
        out["WhatIfForecastArn"] = value["what_if_forecast_arn"]
    if "what_if_analysis_arn" in value:
        out["WhatIfAnalysisArn"] = value["what_if_analysis_arn"]
    if "estimated_time_remaining_in_minutes" in value:
        out["EstimatedTimeRemainingInMinutes"] = value[
            "estimated_time_remaining_in_minutes"
        ]
    if "status" in value:
        out["Status"] = value["status"]
    if "message" in value:
        out["Message"] = value["message"]
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
    if "time_series_transformations" in value:
        import aws_sdk_forecast.types.time_series_transformations

        out["TimeSeriesTransformations"] = (
            aws_sdk_forecast.types.time_series_transformations.serialize_aws_json_1_1(
                value["time_series_transformations"]
            )
        )
    if "time_series_replacements_data_source" in value:
        import aws_sdk_forecast.types.time_series_replacements_data_source

        out["TimeSeriesReplacementsDataSource"] = (
            aws_sdk_forecast.types.time_series_replacements_data_source.serialize_aws_json_1_1(
                value["time_series_replacements_data_source"]
            )
        )
    if "forecast_types" in value:
        import aws_sdk_forecast.types.forecast_types

        out["ForecastTypes"] = (
            aws_sdk_forecast.types.forecast_types.serialize_aws_json_1_1(
                value["forecast_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWhatIfForecastResponse:
    out: DescribeWhatIfForecastResponse = {}  # type: ignore[typeddict-item]
    if "WhatIfForecastName" in data:
        out["what_if_forecast_name"] = data["WhatIfForecastName"]
    if "WhatIfForecastArn" in data:
        out["what_if_forecast_arn"] = data["WhatIfForecastArn"]
    if "WhatIfAnalysisArn" in data:
        out["what_if_analysis_arn"] = data["WhatIfAnalysisArn"]
    if "EstimatedTimeRemainingInMinutes" in data:
        out["estimated_time_remaining_in_minutes"] = data[
            "EstimatedTimeRemainingInMinutes"
        ]
    if "Status" in data:
        out["status"] = data["Status"]
    if "Message" in data:
        out["message"] = data["Message"]
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
    if "TimeSeriesTransformations" in data:
        import aws_sdk_forecast.types.time_series_transformations

        out["time_series_transformations"] = (
            aws_sdk_forecast.types.time_series_transformations.deserialize_aws_json_1_1(
                data["TimeSeriesTransformations"]
            )
        )
    if "TimeSeriesReplacementsDataSource" in data:
        import aws_sdk_forecast.types.time_series_replacements_data_source

        out["time_series_replacements_data_source"] = (
            aws_sdk_forecast.types.time_series_replacements_data_source.deserialize_aws_json_1_1(
                data["TimeSeriesReplacementsDataSource"]
            )
        )
    if "ForecastTypes" in data:
        import aws_sdk_forecast.types.forecast_types

        out["forecast_types"] = (
            aws_sdk_forecast.types.forecast_types.deserialize_aws_json_1_1(
                data["ForecastTypes"]
            )
        )
    return out
