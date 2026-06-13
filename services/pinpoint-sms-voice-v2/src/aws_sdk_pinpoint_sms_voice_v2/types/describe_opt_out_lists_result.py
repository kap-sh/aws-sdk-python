"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeOptOutListsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_information_list


class DescribeOptOutListsResult(TypedDict):
    opt_out_lists: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_information_list.OptOutListInformationList"
    ]
    """<p>An array of OptOutListInformation objects that contain the details for the requested OptOutLists.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. If this field is empty then there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeOptOutListsResult) -> dict:
    out: dict = {}
    if "opt_out_lists" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_information_list

        out["OptOutLists"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_information_list.serialize_aws_json_1_0(
                value["opt_out_lists"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeOptOutListsResult:
    out: DescribeOptOutListsResult = {}  # type: ignore[typeddict-item]
    if "OptOutLists" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_information_list

        out["opt_out_lists"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_information_list.deserialize_aws_json_1_0(
                data["OptOutLists"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
