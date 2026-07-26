"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeOptOutListsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.max_results
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.opt_out_list_name_list
    import capo_pinpoint_sms_voice_v2.types.owner


class DescribeOptOutListsRequest(TypedDict, closed=True):
    opt_out_list_names: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.opt_out_list_name_list.OptOutListNameList"
    ]
    """<p>The OptOutLists to show the details of. This is an array of strings that can be either the OptOutListName or OptOutListArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""
    max_results: NotRequired["capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per each request.</p>"""
    owner: NotRequired["capo_pinpoint_sms_voice_v2.types.owner.Owner"]
    """<p>Use <code>SELF</code> to filter the list of Opt-Out List to ones your account owns or use <code>SHARED</code> to filter on Opt-Out List shared with your account. The <code>Owner</code> and <code>OptOutListNames</code> parameters can't be used at the same time.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeOptOutListsRequest) -> dict:
    out: dict = {}
    if "opt_out_list_names" in value:
        import capo_pinpoint_sms_voice_v2.types.opt_out_list_name_list

        out["OptOutListNames"] = (
            capo_pinpoint_sms_voice_v2.types.opt_out_list_name_list.serialize_aws_json_1_0(
                value["opt_out_list_names"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeOptOutListsRequest:
    out: DescribeOptOutListsRequest = {}  # type: ignore[typeddict-item]
    if "OptOutListNames" in data:
        import capo_pinpoint_sms_voice_v2.types.opt_out_list_name_list

        out["opt_out_list_names"] = (
            capo_pinpoint_sms_voice_v2.types.opt_out_list_name_list.deserialize_aws_json_1_0(
                data["OptOutListNames"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "Owner" in data:
        out["owner"] = data["Owner"]
    return out
