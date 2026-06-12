"""Generated from Smithy shape ``com.amazonaws.workmail#PutMobileDeviceAccessOverrideRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.device_id
    import aws_sdk_workmail.types.entity_identifier
    import aws_sdk_workmail.types.mobile_device_access_rule_description
    import aws_sdk_workmail.types.mobile_device_access_rule_effect
    import aws_sdk_workmail.types.organization_id


class PutMobileDeviceAccessOverrideRequest(TypedDict):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>Identifies the WorkMail organization for which you create the override.</p>"""
    user_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The WorkMail user for which you create the override. Accepts the following types of user identities:</p> <ul> <li> <p>User ID: <code>12345678-1234-1234-1234-123456789012</code> or <code>S-1-1-12-1234567890-123456789-123456789-1234</code> </p> </li> <li> <p>Email address: <code>user@domain.tld</code> </p> </li> <li> <p>User name: <code>user</code> </p> </li> </ul>"""
    device_id: "aws_sdk_workmail.types.device_id.DeviceId"
    """<p>The mobile device for which you create the override. <code>DeviceId</code> is case insensitive.</p>"""
    effect: "aws_sdk_workmail.types.mobile_device_access_rule_effect.MobileDeviceAccessRuleEffect"
    """<p>The effect of the override, <code>ALLOW</code> or <code>DENY</code>.</p>"""
    description: NotRequired[
        "aws_sdk_workmail.types.mobile_device_access_rule_description.MobileDeviceAccessRuleDescription"
    ]
    """<p>A description of the override.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutMobileDeviceAccessOverrideRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["UserId"] = value["user_id"]
    out["DeviceId"] = value["device_id"]
    import aws_sdk_workmail.types.mobile_device_access_rule_effect

    out["Effect"] = (
        aws_sdk_workmail.types.mobile_device_access_rule_effect.serialize_aws_json_1_1(
            value["effect"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutMobileDeviceAccessOverrideRequest:
    out: PutMobileDeviceAccessOverrideRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "PutMobileDeviceAccessOverrideRequest.organization_id required"
        )
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError(
            "PutMobileDeviceAccessOverrideRequest.user_id required"
        )
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    else:
        raise DeserializationError(
            "PutMobileDeviceAccessOverrideRequest.device_id required"
        )
    if "Effect" in data:
        import aws_sdk_workmail.types.mobile_device_access_rule_effect

        out["effect"] = (
            aws_sdk_workmail.types.mobile_device_access_rule_effect.deserialize_aws_json_1_1(
                data["Effect"]
            )
        )
    else:
        raise DeserializationError(
            "PutMobileDeviceAccessOverrideRequest.effect required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    return out
