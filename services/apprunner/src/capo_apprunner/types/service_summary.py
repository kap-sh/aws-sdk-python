"""Generated from Smithy shape ``com.amazonaws.apprunner#ServiceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.app_runner_resource_arn
    import capo_apprunner.types.service_id
    import capo_apprunner.types.service_name
    import capo_apprunner.types.service_status
    import capo_apprunner.types.string
    import capo_apprunner.types.timestamp


class ServiceSummary(TypedDict, closed=True):
    service_name: NotRequired["capo_apprunner.types.service_name.ServiceName"]
    """<p>The customer-provided service name.</p>"""
    service_id: NotRequired["capo_apprunner.types.service_id.ServiceId"]
    """<p>An ID that App Runner generated for this service. It's unique within the Amazon Web Services Region.</p>"""
    service_arn: NotRequired[
        "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of this service.</p>"""
    service_url: NotRequired["capo_apprunner.types.string.String"]
    """<p>A subdomain URL that App Runner generated for this service. You can use this URL to access your service web application.</p>"""
    created_at: NotRequired["capo_apprunner.types.timestamp.Timestamp"]
    """<p>The time when the App Runner service was created. It's in the Unix time stamp format.</p>"""
    updated_at: NotRequired["capo_apprunner.types.timestamp.Timestamp"]
    """<p>The time when the App Runner service was last updated. It's in theUnix time stamp format.</p>"""
    status: NotRequired["capo_apprunner.types.service_status.ServiceStatus"]
    """<p>The current state of the App Runner service. These particular values mean the following.</p> <ul> <li> <p> <code>CREATE_FAILED</code> – The service failed to create. The failed service isn't usable, and still counts towards your service quota. To troubleshoot this failure, read the failure events and logs, change any parameters that need to be fixed, and rebuild your service using <code>UpdateService</code>.</p> </li> <li> <p> <code>DELETE_FAILED</code> – The service failed to delete and can't be successfully recovered. Retry the service deletion call to ensure that all related resources are removed.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceSummary) -> dict:
    out: dict = {}
    if "service_name" in value:
        out["ServiceName"] = value["service_name"]
    if "service_id" in value:
        out["ServiceId"] = value["service_id"]
    if "service_arn" in value:
        out["ServiceArn"] = value["service_arn"]
    if "service_url" in value:
        out["ServiceUrl"] = value["service_url"]
    if "created_at" in value:
        import capo_apprunner.types.timestamp

        out["CreatedAt"] = capo_apprunner.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_apprunner.types.timestamp

        out["UpdatedAt"] = capo_apprunner.types.timestamp.serialize_aws_json_1_0(
            value["updated_at"]
        )
    if "status" in value:
        import capo_apprunner.types.service_status

        out["Status"] = capo_apprunner.types.service_status.serialize_aws_json_1_0(
            value["status"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceSummary:
    out: ServiceSummary = {}  # type: ignore[typeddict-item]
    if "ServiceName" in data:
        out["service_name"] = data["ServiceName"]
    if "ServiceId" in data:
        out["service_id"] = data["ServiceId"]
    if "ServiceArn" in data:
        out["service_arn"] = data["ServiceArn"]
    if "ServiceUrl" in data:
        out["service_url"] = data["ServiceUrl"]
    if "CreatedAt" in data:
        import capo_apprunner.types.timestamp

        out["created_at"] = capo_apprunner.types.timestamp.deserialize_aws_json_1_0(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import capo_apprunner.types.timestamp

        out["updated_at"] = capo_apprunner.types.timestamp.deserialize_aws_json_1_0(
            data["UpdatedAt"]
        )
    if "Status" in data:
        import capo_apprunner.types.service_status

        out["status"] = capo_apprunner.types.service_status.deserialize_aws_json_1_0(
            data["Status"]
        )
    return out
