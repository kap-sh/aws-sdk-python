"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ReleaseSenderIdResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code
    import aws_sdk_pinpoint_sms_voice_v2.types.message_type_list
    import aws_sdk_pinpoint_sms_voice_v2.types.sender_id


class ReleaseSenderIdResult(TypedDict):
    sender_id_arn: "str"
    """<p>The Amazon Resource Name (ARN) associated with the SenderId.</p>"""
    sender_id: "aws_sdk_pinpoint_sms_voice_v2.types.sender_id.SenderId"
    """<p>The sender ID that was released.</p>"""
    iso_country_code: (
        "aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
    )
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.</p>"""
    message_types: (
        "aws_sdk_pinpoint_sms_voice_v2.types.message_type_list.MessageTypeList"
    )
    """<p>The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.</p>"""
    monthly_leasing_price: "str"
    """<p>The monthly price, in US dollars, to lease the sender ID.</p>"""
    registered: "bool"
    """<p>True if the sender ID is registered.</p>"""
    registration_id: NotRequired["str"]
    """<p>The unique identifier for the registration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReleaseSenderIdResult) -> dict:
    out: dict = {}
    out["SenderIdArn"] = value["sender_id_arn"]
    out["SenderId"] = value["sender_id"]
    out["IsoCountryCode"] = value["iso_country_code"]
    import aws_sdk_pinpoint_sms_voice_v2.types.message_type_list

    out["MessageTypes"] = (
        aws_sdk_pinpoint_sms_voice_v2.types.message_type_list.serialize_aws_json_1_0(
            value["message_types"]
        )
    )
    out["MonthlyLeasingPrice"] = value["monthly_leasing_price"]
    out["Registered"] = value.get("registered", False)
    if "registration_id" in value:
        out["RegistrationId"] = value["registration_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ReleaseSenderIdResult:
    out: ReleaseSenderIdResult = {}  # type: ignore[typeddict-item]
    if "SenderIdArn" in data:
        out["sender_id_arn"] = data["SenderIdArn"]
    else:
        raise DeserializationError("ReleaseSenderIdResult.sender_id_arn required")
    if "SenderId" in data:
        out["sender_id"] = data["SenderId"]
    else:
        raise DeserializationError("ReleaseSenderIdResult.sender_id required")
    if "IsoCountryCode" in data:
        out["iso_country_code"] = data["IsoCountryCode"]
    else:
        raise DeserializationError("ReleaseSenderIdResult.iso_country_code required")
    if "MessageTypes" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.message_type_list

        out["message_types"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.message_type_list.deserialize_aws_json_1_0(
                data["MessageTypes"]
            )
        )
    else:
        raise DeserializationError("ReleaseSenderIdResult.message_types required")
    if "MonthlyLeasingPrice" in data:
        out["monthly_leasing_price"] = data["MonthlyLeasingPrice"]
    else:
        raise DeserializationError(
            "ReleaseSenderIdResult.monthly_leasing_price required"
        )
    if "Registered" in data:
        out["registered"] = data["Registered"]
    else:
        out["registered"] = False
    if "RegistrationId" in data:
        out["registration_id"] = data["RegistrationId"]
    return out
