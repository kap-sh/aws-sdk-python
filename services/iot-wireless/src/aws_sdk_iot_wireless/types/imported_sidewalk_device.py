"""Generated from Smithy shape ``com.amazonaws.iotwireless#ImportedSidewalkDevice``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.last_update_time
    import aws_sdk_iot_wireless.types.onboard_status
    import aws_sdk_iot_wireless.types.onboard_status_reason
    import aws_sdk_iot_wireless.types.sidewalk_manufacturing_sn


class ImportedSidewalkDevice(TypedDict):
    sidewalk_manufacturing_sn: NotRequired[
        "aws_sdk_iot_wireless.types.sidewalk_manufacturing_sn.SidewalkManufacturingSn"
    ]
    """<p>The Sidewalk manufacturing serial number (SMSN) of the Sidewalk device.</p>"""
    onboarding_status: NotRequired[
        "aws_sdk_iot_wireless.types.onboard_status.OnboardStatus"
    ]
    """<p>The onboarding status of the Sidewalk device in the import task.</p>"""
    onboarding_status_reason: NotRequired[
        "aws_sdk_iot_wireless.types.onboard_status_reason.OnboardStatusReason"
    ]
    """<p>The reason for the onboarding status information for the Sidewalk device.</p>"""
    last_update_time: NotRequired[
        "aws_sdk_iot_wireless.types.last_update_time.LastUpdateTime"
    ]
    """<p>The time at which the status information was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportedSidewalkDevice) -> dict:
    out: dict = {}
    if "sidewalk_manufacturing_sn" in value:
        out["SidewalkManufacturingSn"] = value["sidewalk_manufacturing_sn"]
    if "onboarding_status" in value:
        import aws_sdk_iot_wireless.types.onboard_status

        out["OnboardingStatus"] = (
            aws_sdk_iot_wireless.types.onboard_status.serialize_json(
                value["onboarding_status"]
            )
        )
    if "onboarding_status_reason" in value:
        out["OnboardingStatusReason"] = value["onboarding_status_reason"]
    if "last_update_time" in value:
        import aws_sdk_iot_wireless.types.last_update_time

        out["LastUpdateTime"] = (
            aws_sdk_iot_wireless.types.last_update_time.serialize_json(
                value["last_update_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImportedSidewalkDevice:
    out: ImportedSidewalkDevice = {}  # type: ignore[typeddict-item]
    if "SidewalkManufacturingSn" in data:
        out["sidewalk_manufacturing_sn"] = data["SidewalkManufacturingSn"]
    if "OnboardingStatus" in data:
        import aws_sdk_iot_wireless.types.onboard_status

        out["onboarding_status"] = (
            aws_sdk_iot_wireless.types.onboard_status.deserialize_json(
                data["OnboardingStatus"]
            )
        )
    if "OnboardingStatusReason" in data:
        out["onboarding_status_reason"] = data["OnboardingStatusReason"]
    if "LastUpdateTime" in data:
        import aws_sdk_iot_wireless.types.last_update_time

        out["last_update_time"] = (
            aws_sdk_iot_wireless.types.last_update_time.deserialize_json(
                data["LastUpdateTime"]
            )
        )
    return out
