"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#UpdateSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_license_manager_user_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.security_group
    import aws_sdk_license_manager_user_subscriptions.types.subnets


class UpdateSettings(TypedDict):
    add_subnets: "aws_sdk_license_manager_user_subscriptions.types.subnets.Subnets"
    """<p>The ID of one or more subnets in which License Manager will create a VPC endpoint for products that require connectivity to activation servers.</p>"""
    remove_subnets: "aws_sdk_license_manager_user_subscriptions.types.subnets.Subnets"
    """<p>The ID of one or more subnets to remove.</p>"""
    security_group_id: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.security_group.SecurityGroup"
    ]
    """<p>A security group ID that allows inbound TCP port 1688 communication between resources in your VPC and the VPC endpoints for activation servers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSettings) -> dict:
    out: dict = {}
    import aws_sdk_license_manager_user_subscriptions.types.subnets

    out["AddSubnets"] = (
        aws_sdk_license_manager_user_subscriptions.types.subnets.serialize_json(
            value["add_subnets"]
        )
    )
    import aws_sdk_license_manager_user_subscriptions.types.subnets

    out["RemoveSubnets"] = (
        aws_sdk_license_manager_user_subscriptions.types.subnets.serialize_json(
            value["remove_subnets"]
        )
    )
    if "security_group_id" in value:
        out["SecurityGroupId"] = value["security_group_id"]
    return out


def deserialize_json(data: dict) -> UpdateSettings:
    out: UpdateSettings = {}  # type: ignore[typeddict-item]
    if "AddSubnets" in data:
        import aws_sdk_license_manager_user_subscriptions.types.subnets

        out["add_subnets"] = (
            aws_sdk_license_manager_user_subscriptions.types.subnets.deserialize_json(
                data["AddSubnets"]
            )
        )
    else:
        raise DeserializationError("UpdateSettings.add_subnets required")
    if "RemoveSubnets" in data:
        import aws_sdk_license_manager_user_subscriptions.types.subnets

        out["remove_subnets"] = (
            aws_sdk_license_manager_user_subscriptions.types.subnets.deserialize_json(
                data["RemoveSubnets"]
            )
        )
    else:
        raise DeserializationError("UpdateSettings.remove_subnets required")
    if "SecurityGroupId" in data:
        out["security_group_id"] = data["SecurityGroupId"]
    return out
