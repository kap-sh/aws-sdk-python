"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DestinationCountryParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.destination_country_parameter_key
    import aws_sdk_pinpoint_sms_voice_v2.types.destination_country_parameter_value

DestinationCountryParameters: TypeAlias = dict[
    "aws_sdk_pinpoint_sms_voice_v2.types.destination_country_parameter_key.DestinationCountryParameterKey",
    "aws_sdk_pinpoint_sms_voice_v2.types.destination_country_parameter_value.DestinationCountryParameterValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: DestinationCountryParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> DestinationCountryParameters:
    out: DestinationCountryParameters = {}
    for key, value in data.items():
        out[key] = value
    return out
