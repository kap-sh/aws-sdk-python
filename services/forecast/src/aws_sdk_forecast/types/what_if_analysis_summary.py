"""Generated from Smithy shape ``com.amazonaws.forecast#WhatIfAnalysisSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn
    import aws_sdk_forecast.types.error_message
    import aws_sdk_forecast.types.name
    import aws_sdk_forecast.types.status
    import aws_sdk_forecast.types.timestamp


class WhatIfAnalysisSummary(TypedDict, closed=True):
    what_if_analysis_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the what-if analysis.</p>"""
    what_if_analysis_name: NotRequired["aws_sdk_forecast.types.name.Name"]
    """<p>The name of the what-if analysis.</p>"""
    forecast_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the baseline forecast that is being used in this what-if analysis.</p>"""
    status: NotRequired["aws_sdk_forecast.types.status.Status"]
    """<p>The status of the what-if analysis. States include:</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>CREATE_STOPPING</code>, <code>CREATE_STOPPED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> </ul> <note> <p>The <code>Status</code> of the what-if analysis must be <code>ACTIVE</code> before you can access the analysis.</p> </note>"""
    message: NotRequired["aws_sdk_forecast.types.error_message.ErrorMessage"]
    """<p>If an error occurred, an informational message about the error.</p>"""
    creation_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>When the what-if analysis was created.</p>"""
    last_modification_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>The last time the resource was modified. The timestamp depends on the status of the job:</p> <ul> <li> <p> <code>CREATE_PENDING</code> - The <code>CreationTime</code>.</p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPING</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPED</code> - When the job stopped.</p> </li> <li> <p> <code>ACTIVE</code> or <code>CREATE_FAILED</code> - When the job finished or failed.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WhatIfAnalysisSummary) -> dict:
    out: dict = {}
    if "what_if_analysis_arn" in value:
        out["WhatIfAnalysisArn"] = value["what_if_analysis_arn"]
    if "what_if_analysis_name" in value:
        out["WhatIfAnalysisName"] = value["what_if_analysis_name"]
    if "forecast_arn" in value:
        out["ForecastArn"] = value["forecast_arn"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> WhatIfAnalysisSummary:
    out: WhatIfAnalysisSummary = {}  # type: ignore[typeddict-item]
    if "WhatIfAnalysisArn" in data:
        out["what_if_analysis_arn"] = data["WhatIfAnalysisArn"]
    if "WhatIfAnalysisName" in data:
        out["what_if_analysis_name"] = data["WhatIfAnalysisName"]
    if "ForecastArn" in data:
        out["forecast_arn"] = data["ForecastArn"]
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
    return out
