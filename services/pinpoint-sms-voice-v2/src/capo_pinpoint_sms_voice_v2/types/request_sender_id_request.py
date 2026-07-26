"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RequestSenderIdRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.client_token
    import capo_pinpoint_sms_voice_v2.types.iso_country_code
    import capo_pinpoint_sms_voice_v2.types.message_type_list
    import capo_pinpoint_sms_voice_v2.types.sender_id
    import capo_pinpoint_sms_voice_v2.types.tag_list


class RequestSenderIdRequest(TypedDict, closed=True):
    sender_id: "capo_pinpoint_sms_voice_v2.types.sender_id.SenderId"
    """<p>The sender ID string to request.</p>"""
    iso_country_code: "capo_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.</p>"""
    message_types: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.message_type_list.MessageTypeList"
    ]
    """<p>The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.</p>"""
    deletion_protection_enabled: NotRequired["bool"]
    """<p>By default this is set to false. When set to true the sender ID can't be deleted.</p>"""
    tags: NotRequired["capo_pinpoint_sms_voice_v2.types.tag_list.TagList"]
    """<p>An array of tags (key and value pairs) to associate with the sender ID.</p>"""
    client_token: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RequestSenderIdRequest) -> dict:
    out: dict = {}
    out["SenderId"] = value["sender_id"]
    out["IsoCountryCode"] = value["iso_country_code"]
    if "message_types" in value:
        import capo_pinpoint_sms_voice_v2.types.message_type_list

        out["MessageTypes"] = (
            capo_pinpoint_sms_voice_v2.types.message_type_list.serialize_aws_json_1_0(
                value["message_types"]
            )
        )
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


def deserialize_aws_json_1_0(data: dict) -> RequestSenderIdRequest:
    out: RequestSenderIdRequest = {}  # type: ignore[typeddict-item]
    if "SenderId" in data:
        out["sender_id"] = data["SenderId"]
    else:
        raise DeserializationError("RequestSenderIdRequest.sender_id required")
    if "IsoCountryCode" in data:
        out["iso_country_code"] = data["IsoCountryCode"]
    else:
        raise DeserializationError("RequestSenderIdRequest.iso_country_code required")
    if "MessageTypes" in data:
        import capo_pinpoint_sms_voice_v2.types.message_type_list

        out["message_types"] = (
            capo_pinpoint_sms_voice_v2.types.message_type_list.deserialize_aws_json_1_0(
                data["MessageTypes"]
            )
        )
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
