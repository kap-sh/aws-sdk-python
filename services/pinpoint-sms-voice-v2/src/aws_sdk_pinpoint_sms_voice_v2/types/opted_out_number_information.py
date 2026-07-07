"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#OptedOutNumberInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_pinpoint_sms_voice_v2.types.phone_number


class OptedOutNumberInformation(TypedDict, closed=True):
    opted_out_number: "aws_sdk_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
    """<p>The phone number that is opted out.</p>"""
    opted_out_timestamp: "datetime.datetime"
    r"""<p>The time that the op tout occurred, in <a href=\"https://www.epochconverter.com/\">UNIX epoch time</a> format.</p>"""
    end_user_opted_out: "bool"
    """<p>This is set to true if it was the end recipient that opted out.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OptedOutNumberInformation) -> dict:
    out: dict = {}
    out["OptedOutNumber"] = value["opted_out_number"]
    import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["OptedOutTimestamp"] = (
        aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["opted_out_timestamp"]
        )
    )
    out["EndUserOptedOut"] = value.get("end_user_opted_out", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> OptedOutNumberInformation:
    out: OptedOutNumberInformation = {}  # type: ignore[typeddict-item]
    if "OptedOutNumber" in data:
        out["opted_out_number"] = data["OptedOutNumber"]
    else:
        raise DeserializationError(
            "OptedOutNumberInformation.opted_out_number required"
        )
    if "OptedOutTimestamp" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["opted_out_timestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["OptedOutTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "OptedOutNumberInformation.opted_out_timestamp required"
        )
    if "EndUserOptedOut" in data:
        out["end_user_opted_out"] = data["EndUserOptedOut"]
    else:
        out["end_user_opted_out"] = False
    return out
