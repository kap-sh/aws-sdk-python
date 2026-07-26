"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RequestPhoneNumberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.client_token
    import capo_pinpoint_sms_voice_v2.types.iso_country_code
    import capo_pinpoint_sms_voice_v2.types.message_type
    import capo_pinpoint_sms_voice_v2.types.number_capability_list
    import capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn
    import capo_pinpoint_sms_voice_v2.types.pool_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.registration_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.requestable_number_type
    import capo_pinpoint_sms_voice_v2.types.tag_list


class RequestPhoneNumberRequest(TypedDict, closed=True):
    iso_country_code: "capo_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region. </p>"""
    message_type: "capo_pinpoint_sms_voice_v2.types.message_type.MessageType"
    """<p>The type of message. Valid values are <code>TRANSACTIONAL</code> for messages that are critical or time-sensitive and <code>PROMOTIONAL</code> for messages that aren't critical or time-sensitive.</p>"""
    number_capabilities: (
        "capo_pinpoint_sms_voice_v2.types.number_capability_list.NumberCapabilityList"
    )
    """<p>Indicates if the phone number will be used for text messages, voice messages, or both. </p>"""
    number_type: (
        "capo_pinpoint_sms_voice_v2.types.requestable_number_type.RequestableNumberType"
    )
    """<p>The type of phone number to request.</p> <p>When you request a <code>SIMULATOR</code> phone number, you must set <b>MessageType</b> as <code>TRANSACTIONAL</code>. </p>"""
    opt_out_list_name: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn.OptOutListNameOrArn"
    ]
    """<p>The name of the OptOutList to associate with the phone number. You can use the OptOutListName or OptOutListArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    pool_id: NotRequired["capo_pinpoint_sms_voice_v2.types.pool_id_or_arn.PoolIdOrArn"]
    """<p>The pool to associated with the phone number. You can use the PoolId or PoolArn. </p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    registration_id: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn"
    ]
    """<p>Use this field to attach your phone number for an external registration process.</p>"""
    international_sending_enabled: NotRequired["bool"]
    """<p>By default this is set to false. When set to true the international sending of phone number is Enabled. </p>"""
    deletion_protection_enabled: NotRequired["bool"]
    """<p>By default this is set to false. When set to true the phone number can't be deleted.</p>"""
    tags: NotRequired["capo_pinpoint_sms_voice_v2.types.tag_list.TagList"]
    """<p>An array of tags (key and value pairs) to associate with the requested phone number. </p>"""
    client_token: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RequestPhoneNumberRequest) -> dict:
    out: dict = {}
    out["IsoCountryCode"] = value["iso_country_code"]
    out["MessageType"] = value["message_type"]
    import capo_pinpoint_sms_voice_v2.types.number_capability_list

    out["NumberCapabilities"] = (
        capo_pinpoint_sms_voice_v2.types.number_capability_list.serialize_aws_json_1_0(
            value["number_capabilities"]
        )
    )
    out["NumberType"] = value["number_type"]
    if "opt_out_list_name" in value:
        out["OptOutListName"] = value["opt_out_list_name"]
    if "pool_id" in value:
        out["PoolId"] = value["pool_id"]
    if "registration_id" in value:
        out["RegistrationId"] = value["registration_id"]
    if "international_sending_enabled" in value:
        out["InternationalSendingEnabled"] = value["international_sending_enabled"]
    if "deletion_protection_enabled" in value:
        out["DeletionProtectionEnabled"] = value["deletion_protection_enabled"]
    if "tags" in value:
        import capo_pinpoint_sms_voice_v2.types.tag_list

        out["Tags"] = capo_pinpoint_sms_voice_v2.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RequestPhoneNumberRequest:
    out: RequestPhoneNumberRequest = {}  # type: ignore[typeddict-item]
    if "IsoCountryCode" in data:
        out["iso_country_code"] = data["IsoCountryCode"]
    else:
        raise DeserializationError(
            "RequestPhoneNumberRequest.iso_country_code required"
        )
    if "MessageType" in data:
        out["message_type"] = data["MessageType"]
    else:
        raise DeserializationError("RequestPhoneNumberRequest.message_type required")
    if "NumberCapabilities" in data:
        import capo_pinpoint_sms_voice_v2.types.number_capability_list

        out["number_capabilities"] = (
            capo_pinpoint_sms_voice_v2.types.number_capability_list.deserialize_aws_json_1_0(
                data["NumberCapabilities"]
            )
        )
    else:
        raise DeserializationError(
            "RequestPhoneNumberRequest.number_capabilities required"
        )
    if "NumberType" in data:
        out["number_type"] = data["NumberType"]
    else:
        raise DeserializationError("RequestPhoneNumberRequest.number_type required")
    if "OptOutListName" in data:
        out["opt_out_list_name"] = data["OptOutListName"]
    if "PoolId" in data:
        out["pool_id"] = data["PoolId"]
    if "RegistrationId" in data:
        out["registration_id"] = data["RegistrationId"]
    if "InternationalSendingEnabled" in data:
        out["international_sending_enabled"] = data["InternationalSendingEnabled"]
    if "DeletionProtectionEnabled" in data:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    if "Tags" in data:
        import capo_pinpoint_sms_voice_v2.types.tag_list

        out["tags"] = (
            capo_pinpoint_sms_voice_v2.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
