"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ServiceSoftwareOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.boolean
    import aws_sdk_elasticsearch_service.types.deployment_close_date_time_stamp
    import aws_sdk_elasticsearch_service.types.deployment_status
    import aws_sdk_elasticsearch_service.types.string


class ServiceSoftwareOptions(TypedDict, closed=True):
    current_version: NotRequired["aws_sdk_elasticsearch_service.types.string.String"]
    """<p>The current service software version that is present on the domain.</p>"""
    new_version: NotRequired["aws_sdk_elasticsearch_service.types.string.String"]
    """<p>The new service software version if one is available.</p>"""
    update_available: NotRequired["aws_sdk_elasticsearch_service.types.boolean.Boolean"]
    """<p><code>True</code> if you are able to update you service software version. <code>False</code> if you are not able to update your service software version. </p>"""
    cancellable: NotRequired["aws_sdk_elasticsearch_service.types.boolean.Boolean"]
    """<p><code>True</code> if you are able to cancel your service software version update. <code>False</code> if you are not able to cancel your service software version. </p>"""
    update_status: NotRequired[
        "aws_sdk_elasticsearch_service.types.deployment_status.DeploymentStatus"
    ]
    """<p>The status of your service software update. This field can take the following values: <code>ELIGIBLE</code>, <code>PENDING_UPDATE</code>, <code>IN_PROGRESS</code>, <code>COMPLETED</code>, and <code>NOT_ELIGIBLE</code>.</p>"""
    description: NotRequired["aws_sdk_elasticsearch_service.types.string.String"]
    """<p>The description of the <code>UpdateStatus</code>.</p>"""
    automated_update_date: NotRequired[
        "aws_sdk_elasticsearch_service.types.deployment_close_date_time_stamp.DeploymentCloseDateTimeStamp"
    ]
    """<p>Timestamp, in Epoch time, until which you can manually request a service software update. After this date, we automatically update your service software.</p>"""
    optional_deployment: NotRequired[
        "aws_sdk_elasticsearch_service.types.boolean.Boolean"
    ]
    """<p><code>True</code> if a service software is never automatically updated. <code>False</code> if a service software is automatically updated after <code>AutomatedUpdateDate</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceSoftwareOptions) -> dict:
    out: dict = {}
    if "current_version" in value:
        out["CurrentVersion"] = value["current_version"]
    if "new_version" in value:
        out["NewVersion"] = value["new_version"]
    if "update_available" in value:
        out["UpdateAvailable"] = value["update_available"]
    if "cancellable" in value:
        out["Cancellable"] = value["cancellable"]
    if "update_status" in value:
        import aws_sdk_elasticsearch_service.types.deployment_status

        out["UpdateStatus"] = (
            aws_sdk_elasticsearch_service.types.deployment_status.serialize_json(
                value["update_status"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "automated_update_date" in value:
        import aws_sdk_elasticsearch_service.types.deployment_close_date_time_stamp

        out["AutomatedUpdateDate"] = (
            aws_sdk_elasticsearch_service.types.deployment_close_date_time_stamp.serialize_json(
                value["automated_update_date"]
            )
        )
    if "optional_deployment" in value:
        out["OptionalDeployment"] = value["optional_deployment"]
    return out


def deserialize_json(data: dict) -> ServiceSoftwareOptions:
    out: ServiceSoftwareOptions = {}  # type: ignore[typeddict-item]
    if "CurrentVersion" in data:
        out["current_version"] = data["CurrentVersion"]
    if "NewVersion" in data:
        out["new_version"] = data["NewVersion"]
    if "UpdateAvailable" in data:
        out["update_available"] = data["UpdateAvailable"]
    if "Cancellable" in data:
        out["cancellable"] = data["Cancellable"]
    if "UpdateStatus" in data:
        import aws_sdk_elasticsearch_service.types.deployment_status

        out["update_status"] = (
            aws_sdk_elasticsearch_service.types.deployment_status.deserialize_json(
                data["UpdateStatus"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "AutomatedUpdateDate" in data:
        import aws_sdk_elasticsearch_service.types.deployment_close_date_time_stamp

        out["automated_update_date"] = (
            aws_sdk_elasticsearch_service.types.deployment_close_date_time_stamp.deserialize_json(
                data["AutomatedUpdateDate"]
            )
        )
    if "OptionalDeployment" in data:
        out["optional_deployment"] = data["OptionalDeployment"]
    return out
