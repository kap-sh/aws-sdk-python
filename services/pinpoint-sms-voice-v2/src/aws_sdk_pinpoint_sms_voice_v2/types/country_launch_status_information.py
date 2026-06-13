"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CountryLaunchStatusInformation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.carrier_status_information_list
    import aws_sdk_pinpoint_sms_voice_v2.types.country_launch_status
    import aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code


class CountryLaunchStatusInformation(TypedDict):
    iso_country_code: (
        "aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
    )
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.</p>"""
    status: (
        "aws_sdk_pinpoint_sms_voice_v2.types.country_launch_status.CountryLaunchStatus"
    )
    """<p>The launch status for this country.</p>"""
    rcs_platform_id: NotRequired["str"]
    """<p>The RCS platform identifier for this country.</p>"""
    registration_id: "str"
    """<p>The unique identifier of the registration associated with this country launch.</p>"""
    carrier_status: "aws_sdk_pinpoint_sms_voice_v2.types.carrier_status_information_list.CarrierStatusInformationList"
    """<p>An array of CarrierStatusInformation objects containing carrier-level launch status details.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CountryLaunchStatusInformation) -> dict:
    out: dict = {}
    out["IsoCountryCode"] = value["iso_country_code"]
    out["Status"] = value["status"]
    if "rcs_platform_id" in value:
        out["RcsPlatformId"] = value["rcs_platform_id"]
    out["RegistrationId"] = value["registration_id"]
    import aws_sdk_pinpoint_sms_voice_v2.types.carrier_status_information_list

    out["CarrierStatus"] = (
        aws_sdk_pinpoint_sms_voice_v2.types.carrier_status_information_list.serialize_aws_json_1_0(
            value["carrier_status"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CountryLaunchStatusInformation:
    out: CountryLaunchStatusInformation = {}  # type: ignore[typeddict-item]
    if "IsoCountryCode" in data:
        out["iso_country_code"] = data["IsoCountryCode"]
    else:
        raise DeserializationError(
            "CountryLaunchStatusInformation.iso_country_code required"
        )
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("CountryLaunchStatusInformation.status required")
    if "RcsPlatformId" in data:
        out["rcs_platform_id"] = data["RcsPlatformId"]
    if "RegistrationId" in data:
        out["registration_id"] = data["RegistrationId"]
    else:
        raise DeserializationError(
            "CountryLaunchStatusInformation.registration_id required"
        )
    if "CarrierStatus" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.carrier_status_information_list

        out["carrier_status"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.carrier_status_information_list.deserialize_aws_json_1_0(
                data["CarrierStatus"]
            )
        )
    else:
        raise DeserializationError(
            "CountryLaunchStatusInformation.carrier_status required"
        )
    return out
