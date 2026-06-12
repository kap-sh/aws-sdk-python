"""Generated from Smithy shape ``com.amazonaws.deadline#MonitorSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.created_at
    import aws_sdk_deadline.types.created_by
    import aws_sdk_deadline.types.iam_role_arn
    import aws_sdk_deadline.types.identity_center_application_arn
    import aws_sdk_deadline.types.identity_center_instance_arn
    import aws_sdk_deadline.types.monitor_id
    import aws_sdk_deadline.types.region
    import aws_sdk_deadline.types.resource_name
    import aws_sdk_deadline.types.subdomain
    import aws_sdk_deadline.types.updated_at
    import aws_sdk_deadline.types.updated_by
    import aws_sdk_deadline.types.url


class MonitorSummary(TypedDict):
    monitor_id: "aws_sdk_deadline.types.monitor_id.MonitorId"
    """<p>The unique identifier for the monitor.</p>"""
    display_name: "aws_sdk_deadline.types.resource_name.ResourceName"
    """<p>The name of the monitor that displays on the Deadline Cloud console.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    subdomain: "aws_sdk_deadline.types.subdomain.Subdomain"
    """<p>The subdomain used for the monitor URL. The full URL of the monitor is subdomain.Region.deadlinecloud.amazonaws.com.</p>"""
    url: "aws_sdk_deadline.types.url.Url"
    """<p>The complete URL of the monitor. The full URL of the monitor is subdomain.Region.deadlinecloud.amazonaws.com.</p>"""
    role_arn: "aws_sdk_deadline.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name of the IAM role for the monitor. Users of the monitor use this role to access Deadline Cloud resources.</p>"""
    identity_center_instance_arn: (
        "aws_sdk_deadline.types.identity_center_instance_arn.IdentityCenterInstanceArn"
    )
    """<p>The Amazon Resource Name of the IAM Identity Center instance responsible for authenticating monitor users.</p>"""
    identity_center_region: NotRequired["aws_sdk_deadline.types.region.Region"]
    """<p>The Region where IAM Identity Center is enabled.</p>"""
    identity_center_application_arn: "aws_sdk_deadline.types.identity_center_application_arn.IdentityCenterApplicationArn"
    """<p>The Amazon Resource Name that the IAM Identity Center assigned to the monitor when it was created.</p>"""
    created_at: "aws_sdk_deadline.types.created_at.CreatedAt"
    """<p>The UNIX timestamp of the date and time that the monitor was created.</p>"""
    created_by: "aws_sdk_deadline.types.created_by.CreatedBy"
    """<p>The user name of the person that created the monitor.</p>"""
    updated_at: NotRequired["aws_sdk_deadline.types.updated_at.UpdatedAt"]
    """<p>The UNIX timestamp of the date and time that the monitor was last updated.</p>"""
    updated_by: NotRequired["aws_sdk_deadline.types.updated_by.UpdatedBy"]
    """<p>The user name of the person that last updated the monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MonitorSummary) -> dict:
    out: dict = {}
    out["monitorId"] = value["monitor_id"]
    out["displayName"] = value["display_name"]
    out["subdomain"] = value["subdomain"]
    out["url"] = value["url"]
    out["roleArn"] = value["role_arn"]
    out["identityCenterInstanceArn"] = value["identity_center_instance_arn"]
    if "identity_center_region" in value:
        out["identityCenterRegion"] = value["identity_center_region"]
    out["identityCenterApplicationArn"] = value["identity_center_application_arn"]
    import aws_sdk_deadline.types.created_at

    out["createdAt"] = aws_sdk_deadline.types.created_at.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import aws_sdk_deadline.types.updated_at

        out["updatedAt"] = aws_sdk_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    return out


def deserialize_json(data: dict) -> MonitorSummary:
    out: MonitorSummary = {}  # type: ignore[typeddict-item]
    if "monitorId" in data:
        out["monitor_id"] = data["monitorId"]
    else:
        raise DeserializationError("MonitorSummary.monitor_id required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("MonitorSummary.display_name required")
    if "subdomain" in data:
        out["subdomain"] = data["subdomain"]
    else:
        raise DeserializationError("MonitorSummary.subdomain required")
    if "url" in data:
        out["url"] = data["url"]
    else:
        raise DeserializationError("MonitorSummary.url required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("MonitorSummary.role_arn required")
    if "identityCenterInstanceArn" in data:
        out["identity_center_instance_arn"] = data["identityCenterInstanceArn"]
    else:
        raise DeserializationError(
            "MonitorSummary.identity_center_instance_arn required"
        )
    if "identityCenterRegion" in data:
        out["identity_center_region"] = data["identityCenterRegion"]
    if "identityCenterApplicationArn" in data:
        out["identity_center_application_arn"] = data["identityCenterApplicationArn"]
    else:
        raise DeserializationError(
            "MonitorSummary.identity_center_application_arn required"
        )
    if "createdAt" in data:
        import aws_sdk_deadline.types.created_at

        out["created_at"] = aws_sdk_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("MonitorSummary.created_at required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("MonitorSummary.created_by required")
    if "updatedAt" in data:
        import aws_sdk_deadline.types.updated_at

        out["updated_at"] = aws_sdk_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    return out
