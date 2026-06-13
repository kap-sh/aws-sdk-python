"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CreatePoolRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.client_token
    import aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code
    import aws_sdk_pinpoint_sms_voice_v2.types.message_type
    import aws_sdk_pinpoint_sms_voice_v2.types.phone_or_sender_id_or_arn
    import aws_sdk_pinpoint_sms_voice_v2.types.tag_list


class CreatePoolRequest(TypedDict):
    origination_identity: "aws_sdk_pinpoint_sms_voice_v2.types.phone_or_sender_id_or_arn.PhoneOrSenderIdOrArn"
    """<p>The origination identity to use such as a PhoneNumberId, PhoneNumberArn, SenderId or SenderIdArn. You can use <a href=\"https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribePhoneNumbers.html\">DescribePhoneNumbers</a> to find the values for PhoneNumberId and PhoneNumberArn, and use <a href=\"https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeSenderIds.html\">DescribeSenderIds</a> can be used to get the values for SenderId and SenderIdArn.</p> <p>After the pool is created you can add more origination identities to the pool by using <a href=\"https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_AssociateOriginationIdentity.html\">AssociateOriginationIdentity</a>.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    iso_country_code: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
    ]
    """<p>The new two-character code, in ISO 3166-1 alpha-2 format, for the country or region of the new pool. This field is optional and is not required for origination identity types that are not country-specific, such as RCS agents.</p>"""
    message_type: "aws_sdk_pinpoint_sms_voice_v2.types.message_type.MessageType"
    """<p>The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive. After the pool is created the MessageType can't be changed.</p>"""
    deletion_protection_enabled: NotRequired["bool"]
    """<p>By default this is set to false. When set to true the pool can't be deleted. You can change this value using the <a href=\"https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_UpdatePool.html\">UpdatePool</a> action.</p>"""
    tags: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.tag_list.TagList"]
    """<p>An array of tags (key and value pairs) associated with the pool.</p>"""
    client_token: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreatePoolRequest) -> dict:
    out: dict = {}
    out["OriginationIdentity"] = value["origination_identity"]
    if "iso_country_code" in value:
        out["IsoCountryCode"] = value["iso_country_code"]
    out["MessageType"] = value["message_type"]
    if "deletion_protection_enabled" in value:
        out["DeletionProtectionEnabled"] = value["deletion_protection_enabled"]
    if "tags" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.tag_list

        out["Tags"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.tag_list.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreatePoolRequest:
    out: CreatePoolRequest = {}  # type: ignore[typeddict-item]
    if "OriginationIdentity" in data:
        out["origination_identity"] = data["OriginationIdentity"]
    else:
        raise DeserializationError("CreatePoolRequest.origination_identity required")
    if "IsoCountryCode" in data:
        out["iso_country_code"] = data["IsoCountryCode"]
    if "MessageType" in data:
        out["message_type"] = data["MessageType"]
    else:
        raise DeserializationError("CreatePoolRequest.message_type required")
    if "DeletionProtectionEnabled" in data:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    if "Tags" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.tag_list

        out["tags"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
