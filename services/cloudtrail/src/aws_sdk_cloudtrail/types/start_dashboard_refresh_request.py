"""Generated from Smithy shape ``com.amazonaws.cloudtrail#StartDashboardRefreshRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.dashboard_arn
    import aws_sdk_cloudtrail.types.query_parameter_values


class StartDashboardRefreshRequest(TypedDict):
    dashboard_id: "aws_sdk_cloudtrail.types.dashboard_arn.DashboardArn"
    """<p> The name or ARN of the dashboard. </p>"""
    query_parameter_values: NotRequired[
        "aws_sdk_cloudtrail.types.query_parameter_values.QueryParameterValues"
    ]
    """<p> The query parameter values for the dashboard </p> <p>For custom dashboards, the following query parameters are valid: <code>$StartTime$</code>, <code>$EndTime$</code>, and <code>$Period$</code>.</p> <p>For managed dashboards, the following query parameters are valid: <code>$StartTime$</code>, <code>$EndTime$</code>, <code>$Period$</code>, and <code>$EventDataStoreId$</code>. The <code>$EventDataStoreId$</code> query parameter is required.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartDashboardRefreshRequest) -> dict:
    out: dict = {}
    out["DashboardId"] = value["dashboard_id"]
    if "query_parameter_values" in value:
        import aws_sdk_cloudtrail.types.query_parameter_values

        out["QueryParameterValues"] = (
            aws_sdk_cloudtrail.types.query_parameter_values.serialize_aws_json_1_1(
                value["query_parameter_values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartDashboardRefreshRequest:
    out: StartDashboardRefreshRequest = {}  # type: ignore[typeddict-item]
    if "DashboardId" in data:
        out["dashboard_id"] = data["DashboardId"]
    else:
        raise DeserializationError("StartDashboardRefreshRequest.dashboard_id required")
    if "QueryParameterValues" in data:
        import aws_sdk_cloudtrail.types.query_parameter_values

        out["query_parameter_values"] = (
            aws_sdk_cloudtrail.types.query_parameter_values.deserialize_aws_json_1_1(
                data["QueryParameterValues"]
            )
        )
    return out
