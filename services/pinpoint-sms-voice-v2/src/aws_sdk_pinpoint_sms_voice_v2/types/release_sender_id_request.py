"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ReleaseSenderIdRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code
    import aws_sdk_pinpoint_sms_voice_v2.types.sender_id_or_arn


class ReleaseSenderIdRequest(TypedDict):
    sender_id: "aws_sdk_pinpoint_sms_voice_v2.types.sender_id_or_arn.SenderIdOrArn"
    """<p>The sender ID to release.</p>"""
    iso_country_code: (
        "aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
    )
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReleaseSenderIdRequest) -> dict:
    out: dict = {}
    out["SenderId"] = value["sender_id"]
    out["IsoCountryCode"] = value["iso_country_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ReleaseSenderIdRequest:
    out: ReleaseSenderIdRequest = {}  # type: ignore[typeddict-item]
    if "SenderId" in data:
        out["sender_id"] = data["SenderId"]
    else:
        raise DeserializationError("ReleaseSenderIdRequest.sender_id required")
    if "IsoCountryCode" in data:
        out["iso_country_code"] = data["IsoCountryCode"]
    else:
        raise DeserializationError("ReleaseSenderIdRequest.iso_country_code required")
    return out
