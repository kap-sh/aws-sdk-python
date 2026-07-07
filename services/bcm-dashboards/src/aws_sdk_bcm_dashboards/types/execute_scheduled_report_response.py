"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#ExecuteScheduledReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.health_status


class ExecuteScheduledReportResponse(TypedDict, closed=True):
    health_status: NotRequired[
        "aws_sdk_bcm_dashboards.types.health_status.HealthStatus"
    ]
    """<p>The health status of the scheduled report after the execution request.</p>"""
    execution_triggered: NotRequired["bool"]
    """<p>Indicates whether the execution was successfully triggered.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecuteScheduledReportResponse) -> dict:
    out: dict = {}
    if "health_status" in value:
        import aws_sdk_bcm_dashboards.types.health_status

        out["healthStatus"] = (
            aws_sdk_bcm_dashboards.types.health_status.serialize_aws_json_1_0(
                value["health_status"]
            )
        )
    if "execution_triggered" in value:
        out["executionTriggered"] = value["execution_triggered"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExecuteScheduledReportResponse:
    out: ExecuteScheduledReportResponse = {}  # type: ignore[typeddict-item]
    if "healthStatus" in data:
        import aws_sdk_bcm_dashboards.types.health_status

        out["health_status"] = (
            aws_sdk_bcm_dashboards.types.health_status.deserialize_aws_json_1_0(
                data["healthStatus"]
            )
        )
    if "executionTriggered" in data:
        out["execution_triggered"] = data["executionTriggered"]
    return out
