"""Generated from Smithy shape ``com.amazonaws.opensearch#ServiceSoftwareOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.deployment_close_date_time_stamp
    import aws_sdk_opensearch.types.deployment_status
    import aws_sdk_opensearch.types.string


class ServiceSoftwareOptions(TypedDict):
    current_version: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>The current service software version present on the domain.</p>"""
    new_version: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>The new service software version, if one is available.</p>"""
    update_available: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>True if you're able to update your service software version. False if you can't update your service software version.</p>"""
    cancellable: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p> True if you're able to cancel your service software version update. False if you can't cancel your service software update.</p>"""
    update_status: NotRequired[
        "aws_sdk_opensearch.types.deployment_status.DeploymentStatus"
    ]
    """<p>The status of your service software update.</p>"""
    description: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>A description of the service software update status.</p>"""
    automated_update_date: NotRequired[
        "aws_sdk_opensearch.types.deployment_close_date_time_stamp.DeploymentCloseDateTimeStamp"
    ]
    """<p>The timestamp, in Epoch time, until which you can manually request a service software update. After this date, we automatically update your service software.</p>"""
    optional_deployment: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>True if a service software is never automatically updated. False if a service software is automatically updated after the automated update date.</p>"""


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
        import aws_sdk_opensearch.types.deployment_status

        out["UpdateStatus"] = aws_sdk_opensearch.types.deployment_status.serialize_json(
            value["update_status"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "automated_update_date" in value:
        import aws_sdk_opensearch.types.deployment_close_date_time_stamp

        out["AutomatedUpdateDate"] = (
            aws_sdk_opensearch.types.deployment_close_date_time_stamp.serialize_json(
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
        import aws_sdk_opensearch.types.deployment_status

        out["update_status"] = (
            aws_sdk_opensearch.types.deployment_status.deserialize_json(
                data["UpdateStatus"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "AutomatedUpdateDate" in data:
        import aws_sdk_opensearch.types.deployment_close_date_time_stamp

        out["automated_update_date"] = (
            aws_sdk_opensearch.types.deployment_close_date_time_stamp.deserialize_json(
                data["AutomatedUpdateDate"]
            )
        )
    if "OptionalDeployment" in data:
        out["optional_deployment"] = data["OptionalDeployment"]
    return out
