"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SendDestinationNumberVerificationCodeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn
    import aws_sdk_pinpoint_sms_voice_v2.types.context_map
    import aws_sdk_pinpoint_sms_voice_v2.types.destination_country_parameters
    import aws_sdk_pinpoint_sms_voice_v2.types.language_code
    import aws_sdk_pinpoint_sms_voice_v2.types.verification_channel
    import aws_sdk_pinpoint_sms_voice_v2.types.verification_message_origination_identity
    import aws_sdk_pinpoint_sms_voice_v2.types.verified_destination_number_id_or_arn


class SendDestinationNumberVerificationCodeRequest(TypedDict):
    verified_destination_number_id: "aws_sdk_pinpoint_sms_voice_v2.types.verified_destination_number_id_or_arn.VerifiedDestinationNumberIdOrArn"
    """<p>The unique identifier for the verified destination phone number.</p>"""
    verification_channel: (
        "aws_sdk_pinpoint_sms_voice_v2.types.verification_channel.VerificationChannel"
    )
    """<p>Choose to send the verification code as an SMS or voice message.</p>"""
    language_code: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.language_code.LanguageCode"
    ]
    """<p>Choose the language to use for the message.</p>"""
    origination_identity: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.verification_message_origination_identity.VerificationMessageOriginationIdentity"
    ]
    """<p>The origination identity of the message. This can be either the PhoneNumber, PhoneNumberId, PhoneNumberArn, SenderId, SenderIdArn, PoolId, or PoolArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    configuration_set_name: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn"
    ]
    """<p>The name of the configuration set to use. This can be either the ConfigurationSetName or ConfigurationSetArn.</p>"""
    context: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.context_map.ContextMap"]
    """<p>You can specify custom data in this field. If you do, that data is logged to the event destination.</p>"""
    destination_country_parameters: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.destination_country_parameters.DestinationCountryParameters"
    ]
    r"""<p>This field is used for any country-specific registration requirements. Currently, this setting is only used when you send messages to recipients in India using a sender ID. For more information see <a href=\"https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-senderid-india.html\">Special requirements for sending SMS messages to recipients in India</a>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendDestinationNumberVerificationCodeRequest) -> dict:
    out: dict = {}
    out["VerifiedDestinationNumberId"] = value["verified_destination_number_id"]
    out["VerificationChannel"] = value["verification_channel"]
    if "language_code" in value:
        out["LanguageCode"] = value["language_code"]
    if "origination_identity" in value:
        out["OriginationIdentity"] = value["origination_identity"]
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    if "context" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.context_map

        out["Context"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.context_map.serialize_aws_json_1_0(
                value["context"]
            )
        )
    if "destination_country_parameters" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.destination_country_parameters

        out["DestinationCountryParameters"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.destination_country_parameters.serialize_aws_json_1_0(
                value["destination_country_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> SendDestinationNumberVerificationCodeRequest:
    out: SendDestinationNumberVerificationCodeRequest = {}  # type: ignore[typeddict-item]
    if "VerifiedDestinationNumberId" in data:
        out["verified_destination_number_id"] = data["VerifiedDestinationNumberId"]
    else:
        raise DeserializationError(
            "SendDestinationNumberVerificationCodeRequest.verified_destination_number_id required"
        )
    if "VerificationChannel" in data:
        out["verification_channel"] = data["VerificationChannel"]
    else:
        raise DeserializationError(
            "SendDestinationNumberVerificationCodeRequest.verification_channel required"
        )
    if "LanguageCode" in data:
        out["language_code"] = data["LanguageCode"]
    if "OriginationIdentity" in data:
        out["origination_identity"] = data["OriginationIdentity"]
    if "ConfigurationSetName" in data:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    if "Context" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.context_map

        out["context"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.context_map.deserialize_aws_json_1_0(
                data["Context"]
            )
        )
    if "DestinationCountryParameters" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.destination_country_parameters

        out["destination_country_parameters"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.destination_country_parameters.deserialize_aws_json_1_0(
                data["DestinationCountryParameters"]
            )
        )
    return out
