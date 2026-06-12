"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateMonitorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.iam_role_arn
    import aws_sdk_deadline.types.monitor_id
    import aws_sdk_deadline.types.resource_name
    import aws_sdk_deadline.types.subdomain


class UpdateMonitorRequest(TypedDict):
    monitor_id: "aws_sdk_deadline.types.monitor_id.MonitorId"
    """<p>The unique identifier of the monitor to update.</p>"""
    subdomain: NotRequired["aws_sdk_deadline.types.subdomain.Subdomain"]
    """<p>The new value of the subdomain to use when forming the monitor URL.</p>"""
    display_name: NotRequired["aws_sdk_deadline.types.resource_name.ResourceName"]
    """<p>The new value to use for the monitor's display name.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    role_arn: NotRequired["aws_sdk_deadline.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name of the new IAM role to use with the monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMonitorRequest) -> dict:
    out: dict = {}
    if "subdomain" in value:
        out["subdomain"] = value["subdomain"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> UpdateMonitorRequest:
    out: UpdateMonitorRequest = {}  # type: ignore[typeddict-item]
    if "subdomain" in data:
        out["subdomain"] = data["subdomain"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    return out
