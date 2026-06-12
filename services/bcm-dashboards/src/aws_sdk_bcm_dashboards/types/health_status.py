"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#HealthStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.generic_time_stamp
    import aws_sdk_bcm_dashboards.types.health_status_code
    import aws_sdk_bcm_dashboards.types.status_reason_list


class HealthStatus(TypedDict):
    status_code: "aws_sdk_bcm_dashboards.types.health_status_code.HealthStatusCode"
    """<p>The health status code. <code>HEALTHY</code> indicates the scheduled report is configured properly and has all required permissions to execute. <code>UNHEALTHY</code> indicates the scheduled report is unable to deliver the notification to the default Amazon EventBridge EventBus in your account and your action is needed. The reason for the unhealthy state is captured in the health status reasons.</p>"""
    last_refreshed_at: NotRequired[
        "aws_sdk_bcm_dashboards.types.generic_time_stamp.GenericTimeStamp"
    ]
    """<p>The timestamp when the health status was last refreshed.</p>"""
    status_reasons: NotRequired[
        "aws_sdk_bcm_dashboards.types.status_reason_list.StatusReasonList"
    ]
    """<p>The list of reasons for the current health status. Only present when the status is <code>UNHEALTHY</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HealthStatus) -> dict:
    out: dict = {}
    import aws_sdk_bcm_dashboards.types.health_status_code

    out["statusCode"] = (
        aws_sdk_bcm_dashboards.types.health_status_code.serialize_aws_json_1_0(
            value["status_code"]
        )
    )
    if "last_refreshed_at" in value:
        import aws_sdk_bcm_dashboards.types.generic_time_stamp

        out["lastRefreshedAt"] = (
            aws_sdk_bcm_dashboards.types.generic_time_stamp.serialize_aws_json_1_0(
                value["last_refreshed_at"]
            )
        )
    if "status_reasons" in value:
        import aws_sdk_bcm_dashboards.types.status_reason_list

        out["statusReasons"] = (
            aws_sdk_bcm_dashboards.types.status_reason_list.serialize_aws_json_1_0(
                value["status_reasons"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> HealthStatus:
    out: HealthStatus = {}  # type: ignore[typeddict-item]
    if "statusCode" in data:
        import aws_sdk_bcm_dashboards.types.health_status_code

        out["status_code"] = (
            aws_sdk_bcm_dashboards.types.health_status_code.deserialize_aws_json_1_0(
                data["statusCode"]
            )
        )
    else:
        raise DeserializationError("HealthStatus.status_code required")
    if "lastRefreshedAt" in data:
        import aws_sdk_bcm_dashboards.types.generic_time_stamp

        out["last_refreshed_at"] = (
            aws_sdk_bcm_dashboards.types.generic_time_stamp.deserialize_aws_json_1_0(
                data["lastRefreshedAt"]
            )
        )
    if "statusReasons" in data:
        import aws_sdk_bcm_dashboards.types.status_reason_list

        out["status_reasons"] = (
            aws_sdk_bcm_dashboards.types.status_reason_list.deserialize_aws_json_1_0(
                data["statusReasons"]
            )
        )
    return out
