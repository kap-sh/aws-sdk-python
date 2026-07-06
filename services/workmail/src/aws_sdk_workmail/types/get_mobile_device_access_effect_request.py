"""Generated from Smithy shape ``com.amazonaws.workmail#GetMobileDeviceAccessEffectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.device_model
    import aws_sdk_workmail.types.device_operating_system
    import aws_sdk_workmail.types.device_type
    import aws_sdk_workmail.types.device_user_agent
    import aws_sdk_workmail.types.organization_id


class GetMobileDeviceAccessEffectRequest(TypedDict, closed=True):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization to simulate the access effect for.</p>"""
    device_type: NotRequired["aws_sdk_workmail.types.device_type.DeviceType"]
    """<p>Device type the simulated user will report.</p>"""
    device_model: NotRequired["aws_sdk_workmail.types.device_model.DeviceModel"]
    """<p>Device model the simulated user will report.</p>"""
    device_operating_system: NotRequired[
        "aws_sdk_workmail.types.device_operating_system.DeviceOperatingSystem"
    ]
    """<p>Device operating system the simulated user will report.</p>"""
    device_user_agent: NotRequired[
        "aws_sdk_workmail.types.device_user_agent.DeviceUserAgent"
    ]
    """<p>Device user agent the simulated user will report.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMobileDeviceAccessEffectRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    if "device_type" in value:
        out["DeviceType"] = value["device_type"]
    if "device_model" in value:
        out["DeviceModel"] = value["device_model"]
    if "device_operating_system" in value:
        out["DeviceOperatingSystem"] = value["device_operating_system"]
    if "device_user_agent" in value:
        out["DeviceUserAgent"] = value["device_user_agent"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMobileDeviceAccessEffectRequest:
    out: GetMobileDeviceAccessEffectRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "GetMobileDeviceAccessEffectRequest.organization_id required"
        )
    if "DeviceType" in data:
        out["device_type"] = data["DeviceType"]
    if "DeviceModel" in data:
        out["device_model"] = data["DeviceModel"]
    if "DeviceOperatingSystem" in data:
        out["device_operating_system"] = data["DeviceOperatingSystem"]
    if "DeviceUserAgent" in data:
        out["device_user_agent"] = data["DeviceUserAgent"]
    return out
