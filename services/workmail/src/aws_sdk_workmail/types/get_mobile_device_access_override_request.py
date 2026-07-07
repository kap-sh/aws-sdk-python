"""Generated from Smithy shape ``com.amazonaws.workmail#GetMobileDeviceAccessOverrideRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.device_id
    import aws_sdk_workmail.types.entity_identifier
    import aws_sdk_workmail.types.organization_id


class GetMobileDeviceAccessOverrideRequest(TypedDict, closed=True):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization to which you want to apply the override.</p>"""
    user_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier"
    """<p>Identifies the WorkMail user for the override. Accepts the following types of user identities: </p> <ul> <li> <p>User ID: <code>12345678-1234-1234-1234-123456789012</code> or <code>S-1-1-12-1234567890-123456789-123456789-1234</code> </p> </li> <li> <p>Email address: <code>user@domain.tld</code> </p> </li> <li> <p>User name: <code>user</code> </p> </li> </ul>"""
    device_id: "aws_sdk_workmail.types.device_id.DeviceId"
    """<p>The mobile device to which the override applies. <code>DeviceId</code> is case insensitive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMobileDeviceAccessOverrideRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["UserId"] = value["user_id"]
    out["DeviceId"] = value["device_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMobileDeviceAccessOverrideRequest:
    out: GetMobileDeviceAccessOverrideRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "GetMobileDeviceAccessOverrideRequest.organization_id required"
        )
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError(
            "GetMobileDeviceAccessOverrideRequest.user_id required"
        )
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    else:
        raise DeserializationError(
            "GetMobileDeviceAccessOverrideRequest.device_id required"
        )
    return out
