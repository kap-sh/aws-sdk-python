"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteOptOutListResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_name


class DeleteOptOutListResult(TypedDict):
    opt_out_list_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the OptOutList that was removed.</p>"""
    opt_out_list_name: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_name.OptOutListName"
    ]
    """<p>The name of the OptOutList that was removed.</p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    """<p>The time when the OptOutList was created, in <a href=\"https://www.epochconverter.com/\">UNIX epoch time</a> format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteOptOutListResult) -> dict:
    out: dict = {}
    if "opt_out_list_arn" in value:
        out["OptOutListArn"] = value["opt_out_list_arn"]
    if "opt_out_list_name" in value:
        out["OptOutListName"] = value["opt_out_list_name"]
    if "created_timestamp" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["CreatedTimestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteOptOutListResult:
    out: DeleteOptOutListResult = {}  # type: ignore[typeddict-item]
    if "OptOutListArn" in data:
        out["opt_out_list_arn"] = data["OptOutListArn"]
    if "OptOutListName" in data:
        out["opt_out_list_name"] = data["OptOutListName"]
    if "CreatedTimestamp" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    return out
