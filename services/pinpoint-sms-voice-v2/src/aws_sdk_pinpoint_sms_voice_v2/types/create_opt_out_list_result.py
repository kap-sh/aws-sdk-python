"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CreateOptOutListResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_name
    import aws_sdk_pinpoint_sms_voice_v2.types.tag_list


class CreateOptOutListResult(TypedDict, closed=True):
    opt_out_list_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) for the OptOutList.</p>"""
    opt_out_list_name: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_name.OptOutListName"
    ]
    """<p>The name of the new OptOutList.</p>"""
    tags: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.tag_list.TagList"]
    """<p>An array of tags (key and value pairs) associated with the new OptOutList.</p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    r"""<p>The time when the pool was created, in <a href=\"https://www.epochconverter.com/\">UNIX epoch time</a> format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateOptOutListResult) -> dict:
    out: dict = {}
    if "opt_out_list_arn" in value:
        out["OptOutListArn"] = value["opt_out_list_arn"]
    if "opt_out_list_name" in value:
        out["OptOutListName"] = value["opt_out_list_name"]
    if "tags" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.tag_list

        out["Tags"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.tag_list.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    if "created_timestamp" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["CreatedTimestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateOptOutListResult:
    out: CreateOptOutListResult = {}  # type: ignore[typeddict-item]
    if "OptOutListArn" in data:
        out["opt_out_list_arn"] = data["OptOutListArn"]
    if "OptOutListName" in data:
        out["opt_out_list_name"] = data["OptOutListName"]
    if "Tags" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.tag_list

        out["tags"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    if "CreatedTimestamp" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    return out
