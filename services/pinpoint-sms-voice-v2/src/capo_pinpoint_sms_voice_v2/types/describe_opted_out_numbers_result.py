"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeOptedOutNumbersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.opt_out_list_name
    import capo_pinpoint_sms_voice_v2.types.opted_out_number_information_list


class DescribeOptedOutNumbersResult(TypedDict, closed=True):
    opt_out_list_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the OptOutList.</p>"""
    opt_out_list_name: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.opt_out_list_name.OptOutListName"
    ]
    """<p>The name of the OptOutList.</p>"""
    opted_out_numbers: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.opted_out_number_information_list.OptedOutNumberInformationList"
    ]
    """<p>An array of OptedOutNumbersInformation objects that provide information about the requested OptedOutNumbers.</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. If this field is empty then there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeOptedOutNumbersResult) -> dict:
    out: dict = {}
    if "opt_out_list_arn" in value:
        out["OptOutListArn"] = value["opt_out_list_arn"]
    if "opt_out_list_name" in value:
        out["OptOutListName"] = value["opt_out_list_name"]
    if "opted_out_numbers" in value:
        import capo_pinpoint_sms_voice_v2.types.opted_out_number_information_list

        out["OptedOutNumbers"] = (
            capo_pinpoint_sms_voice_v2.types.opted_out_number_information_list.serialize_aws_json_1_0(
                value["opted_out_numbers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeOptedOutNumbersResult:
    out: DescribeOptedOutNumbersResult = {}  # type: ignore[typeddict-item]
    if "OptOutListArn" in data:
        out["opt_out_list_arn"] = data["OptOutListArn"]
    if "OptOutListName" in data:
        out["opt_out_list_name"] = data["OptOutListName"]
    if "OptedOutNumbers" in data:
        import capo_pinpoint_sms_voice_v2.types.opted_out_number_information_list

        out["opted_out_numbers"] = (
            capo_pinpoint_sms_voice_v2.types.opted_out_number_information_list.deserialize_aws_json_1_0(
                data["OptedOutNumbers"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
