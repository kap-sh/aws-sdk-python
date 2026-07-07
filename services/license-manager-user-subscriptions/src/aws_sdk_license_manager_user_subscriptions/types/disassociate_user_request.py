"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#DisassociateUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.arn
    import aws_sdk_license_manager_user_subscriptions.types.identity_provider


class DisassociateUserRequest(TypedDict, closed=True):
    username: NotRequired["str"]
    """<p>The user name from the Active Directory identity provider for the user.</p>"""
    instance_id: NotRequired["str"]
    """<p>The ID of the EC2 instance which provides user-based subscriptions.</p>"""
    identity_provider: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.identity_provider.IdentityProvider"
    ]
    """<p>An object that specifies details for the Active Directory identity provider.</p>"""
    instance_user_arn: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.arn.Arn"
    ]
    """<p>The Amazon Resource Name (ARN) of the user to disassociate from the EC2 instance.</p>"""
    domain: NotRequired["str"]
    """<p>The domain name of the Active Directory that contains information for the user to disassociate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateUserRequest) -> dict:
    out: dict = {}
    if "username" in value:
        out["Username"] = value["username"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "identity_provider" in value:
        import aws_sdk_license_manager_user_subscriptions.types.identity_provider

        out["IdentityProvider"] = (
            aws_sdk_license_manager_user_subscriptions.types.identity_provider.serialize_json(
                value["identity_provider"]
            )
        )
    if "instance_user_arn" in value:
        out["InstanceUserArn"] = value["instance_user_arn"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    return out


def deserialize_json(data: dict) -> DisassociateUserRequest:
    out: DisassociateUserRequest = {}  # type: ignore[typeddict-item]
    if "Username" in data:
        out["username"] = data["Username"]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "IdentityProvider" in data:
        import aws_sdk_license_manager_user_subscriptions.types.identity_provider

        out["identity_provider"] = (
            aws_sdk_license_manager_user_subscriptions.types.identity_provider.deserialize_json(
                data["IdentityProvider"]
            )
        )
    if "InstanceUserArn" in data:
        out["instance_user_arn"] = data["InstanceUserArn"]
    if "Domain" in data:
        out["domain"] = data["Domain"]
    return out
