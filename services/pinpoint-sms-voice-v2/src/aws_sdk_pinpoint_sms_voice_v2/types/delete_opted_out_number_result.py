"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteOptedOutNumberResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_name
    import aws_sdk_pinpoint_sms_voice_v2.types.phone_number


class DeleteOptedOutNumberResult(TypedDict):
    opt_out_list_arn: NotRequired["str"]
    """<p>The OptOutListArn that the phone number was removed from.</p>"""
    opt_out_list_name: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_name.OptOutListName"
    ]
    """<p>The OptOutListName that the phone number was removed from.</p>"""
    opted_out_number: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
    ]
    """<p>The phone number that was removed from the OptOutList.</p>"""
    opted_out_timestamp: NotRequired["datetime.datetime"]
    r"""<p>The time that the number was removed at, in <a href=\"https://www.epochconverter.com/\">UNIX epoch time</a> format.</p>"""
    end_user_opted_out: "bool"
    """<p>This is true if it was the end user who requested their phone number be removed. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteOptedOutNumberResult) -> dict:
    out: dict = {}
    if "opt_out_list_arn" in value:
        out["OptOutListArn"] = value["opt_out_list_arn"]
    if "opt_out_list_name" in value:
        out["OptOutListName"] = value["opt_out_list_name"]
    if "opted_out_number" in value:
        out["OptedOutNumber"] = value["opted_out_number"]
    if "opted_out_timestamp" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["OptedOutTimestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
                value["opted_out_timestamp"]
            )
        )
    out["EndUserOptedOut"] = value.get("end_user_opted_out", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteOptedOutNumberResult:
    out: DeleteOptedOutNumberResult = {}  # type: ignore[typeddict-item]
    if "OptOutListArn" in data:
        out["opt_out_list_arn"] = data["OptOutListArn"]
    if "OptOutListName" in data:
        out["opt_out_list_name"] = data["OptOutListName"]
    if "OptedOutNumber" in data:
        out["opted_out_number"] = data["OptedOutNumber"]
    if "OptedOutTimestamp" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["opted_out_timestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["OptedOutTimestamp"]
            )
        )
    if "EndUserOptedOut" in data:
        out["end_user_opted_out"] = data["EndUserOptedOut"]
    else:
        out["end_user_opted_out"] = False
    return out
