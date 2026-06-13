"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#PutOptedOutNumberRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn
    import aws_sdk_pinpoint_sms_voice_v2.types.phone_number


class PutOptedOutNumberRequest(TypedDict):
    opt_out_list_name: "aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn.OptOutListNameOrArn"
    """<p>The OptOutListName or OptOutListArn to add the phone number to.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    opted_out_number: "aws_sdk_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
    """<p>The phone number to add to the OptOutList in E.164 format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutOptedOutNumberRequest) -> dict:
    out: dict = {}
    out["OptOutListName"] = value["opt_out_list_name"]
    out["OptedOutNumber"] = value["opted_out_number"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutOptedOutNumberRequest:
    out: PutOptedOutNumberRequest = {}  # type: ignore[typeddict-item]
    if "OptOutListName" in data:
        out["opt_out_list_name"] = data["OptOutListName"]
    else:
        raise DeserializationError(
            "PutOptedOutNumberRequest.opt_out_list_name required"
        )
    if "OptedOutNumber" in data:
        out["opted_out_number"] = data["OptedOutNumber"]
    else:
        raise DeserializationError("PutOptedOutNumberRequest.opted_out_number required")
    return out
