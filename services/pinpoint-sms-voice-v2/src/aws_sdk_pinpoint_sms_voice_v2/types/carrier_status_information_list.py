"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CarrierStatusInformationList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.carrier_status_information

CarrierStatusInformationList: TypeAlias = list["aws_sdk_pinpoint_sms_voice_v2.types.carrier_status_information.CarrierStatusInformation"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CarrierStatusInformationList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.carrier_status_information
    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint_sms_voice_v2.types.carrier_status_information.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> CarrierStatusInformationList:
    import aws_sdk_pinpoint_sms_voice_v2.types.carrier_status_information
    out: CarrierStatusInformationList = []
    for item in data:
        out.append(aws_sdk_pinpoint_sms_voice_v2.types.carrier_status_information.deserialize_aws_json_1_0(item))
    return out