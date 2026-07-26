"""Generated from Smithy shape ``com.amazonaws.forecast#WhatIfForecastSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.error_message
    import capo_forecast.types.long_arn
    import capo_forecast.types.name
    import capo_forecast.types.status
    import capo_forecast.types.timestamp


class WhatIfForecastSummary(TypedDict, closed=True):
    what_if_forecast_arn: NotRequired["capo_forecast.types.long_arn.LongArn"]
    """<p>The Amazon Resource Name (ARN) of the what-if forecast.</p>"""
    what_if_forecast_name: NotRequired["capo_forecast.types.name.Name"]
    """<p>The name of the what-if forecast.</p>"""
    what_if_analysis_arn: NotRequired["capo_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the what-if analysis that contains this what-if forecast.</p>"""
    status: NotRequired["capo_forecast.types.status.Status"]
    """<p>The status of the what-if forecast. States include:</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>CREATE_STOPPING</code>, <code>CREATE_STOPPED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> </ul> <note> <p>The <code>Status</code> of the what-if analysis must be <code>ACTIVE</code> before you can access the analysis.</p> </note>"""
    message: NotRequired["capo_forecast.types.error_message.ErrorMessage"]
    """<p>If an error occurred, an informational message about the error.</p>"""
    creation_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>When the what-if forecast was created.</p>"""
    last_modification_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>The last time the resource was modified. The timestamp depends on the status of the job:</p> <ul> <li> <p> <code>CREATE_PENDING</code> - The <code>CreationTime</code>.</p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPING</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPED</code> - When the job stopped.</p> </li> <li> <p> <code>ACTIVE</code> or <code>CREATE_FAILED</code> - When the job finished or failed.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WhatIfForecastSummary) -> dict:
    out: dict = {}
    if "what_if_forecast_arn" in value:
        out["WhatIfForecastArn"] = value["what_if_forecast_arn"]
    if "what_if_forecast_name" in value:
        out["WhatIfForecastName"] = value["what_if_forecast_name"]
    if "what_if_analysis_arn" in value:
        out["WhatIfAnalysisArn"] = value["what_if_analysis_arn"]
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


def deserialize_aws_json_1_1(data: dict) -> WhatIfForecastSummary:
    out: WhatIfForecastSummary = {}  # type: ignore[typeddict-item]
    if "WhatIfForecastArn" in data:
        out["what_if_forecast_arn"] = data["WhatIfForecastArn"]
    if "WhatIfForecastName" in data:
        out["what_if_forecast_name"] = data["WhatIfForecastName"]
    if "WhatIfAnalysisArn" in data:
        out["what_if_analysis_arn"] = data["WhatIfAnalysisArn"]
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
