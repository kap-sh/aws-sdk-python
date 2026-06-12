"""Generated from Smithy shape ``com.amazonaws.deadline#CreateMonitorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.client_token
    import aws_sdk_deadline.types.iam_role_arn
    import aws_sdk_deadline.types.identity_center_instance_arn
    import aws_sdk_deadline.types.region
    import aws_sdk_deadline.types.resource_name
    import aws_sdk_deadline.types.subdomain
    import aws_sdk_deadline.types.tags


class CreateMonitorRequest(TypedDict):
    client_token: NotRequired["aws_sdk_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    display_name: "aws_sdk_deadline.types.resource_name.ResourceName"
    """<p>The name that you give the monitor that is displayed in the Deadline Cloud console.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    identity_center_instance_arn: (
        "aws_sdk_deadline.types.identity_center_instance_arn.IdentityCenterInstanceArn"
    )
    """<p>The Amazon Resource Name of the IAM Identity Center instance that authenticates monitor users.</p>"""
    identity_center_region: NotRequired["aws_sdk_deadline.types.region.Region"]
    """<p>The Region where IAM Identity Center is enabled. Required when IAM Identity Center is in a different Region than the monitor.</p>"""
    subdomain: "aws_sdk_deadline.types.subdomain.Subdomain"
    """<p>The subdomain to use when creating the monitor URL. The full URL of the monitor is subdomain.Region.deadlinecloud.amazonaws.com.</p>"""
    role_arn: "aws_sdk_deadline.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name of the IAM role that the monitor uses to connect to Deadline Cloud. Every user that signs in to the monitor using IAM Identity Center uses this role to access Deadline Cloud resources.</p>"""
    tags: NotRequired["aws_sdk_deadline.types.tags.Tags"]
    """<p>The tags to add to your monitor. Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMonitorRequest) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    out["identityCenterInstanceArn"] = value["identity_center_instance_arn"]
    if "identity_center_region" in value:
        out["identityCenterRegion"] = value["identity_center_region"]
    out["subdomain"] = value["subdomain"]
    out["roleArn"] = value["role_arn"]
    if "tags" in value:
        import aws_sdk_deadline.types.tags

        out["tags"] = aws_sdk_deadline.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateMonitorRequest:
    out: CreateMonitorRequest = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("CreateMonitorRequest.display_name required")
    if "identityCenterInstanceArn" in data:
        out["identity_center_instance_arn"] = data["identityCenterInstanceArn"]
    else:
        raise DeserializationError(
            "CreateMonitorRequest.identity_center_instance_arn required"
        )
    if "identityCenterRegion" in data:
        out["identity_center_region"] = data["identityCenterRegion"]
    if "subdomain" in data:
        out["subdomain"] = data["subdomain"]
    else:
        raise DeserializationError("CreateMonitorRequest.subdomain required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateMonitorRequest.role_arn required")
    if "tags" in data:
        import aws_sdk_deadline.types.tags

        out["tags"] = aws_sdk_deadline.types.tags.deserialize_json(data["tags"])
    return out
