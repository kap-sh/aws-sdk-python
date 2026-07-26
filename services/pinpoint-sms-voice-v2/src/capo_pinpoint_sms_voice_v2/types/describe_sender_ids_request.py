"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeSenderIdsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.max_results
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.owner
    import capo_pinpoint_sms_voice_v2.types.sender_id_filter_list
    import capo_pinpoint_sms_voice_v2.types.sender_id_list


class DescribeSenderIdsRequest(TypedDict, closed=True):
    sender_ids: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.sender_id_list.SenderIdList"
    ]
    """<p>An array of SenderIdAndCountry objects to search for.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    filters: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.sender_id_filter_list.SenderIdFilterList"
    ]
    """<p>An array of SenderIdFilter objects to filter the results.</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""
    max_results: NotRequired["capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per each request.</p>"""
    owner: NotRequired["capo_pinpoint_sms_voice_v2.types.owner.Owner"]
    """<p>Use <code>SELF</code> to filter the list of Sender Ids to ones your account owns or use <code>SHARED</code> to filter on Sender Ids shared with your account. The <code>Owner</code> and <code>SenderIds</code> parameters can't be used at the same time. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeSenderIdsRequest) -> dict:
    out: dict = {}
    if "sender_ids" in value:
        import capo_pinpoint_sms_voice_v2.types.sender_id_list

        out["SenderIds"] = (
            capo_pinpoint_sms_voice_v2.types.sender_id_list.serialize_aws_json_1_0(
                value["sender_ids"]
            )
        )
    if "filters" in value:
        import capo_pinpoint_sms_voice_v2.types.sender_id_filter_list

        out["Filters"] = (
            capo_pinpoint_sms_voice_v2.types.sender_id_filter_list.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeSenderIdsRequest:
    out: DescribeSenderIdsRequest = {}  # type: ignore[typeddict-item]
    if "SenderIds" in data:
        import capo_pinpoint_sms_voice_v2.types.sender_id_list

        out["sender_ids"] = (
            capo_pinpoint_sms_voice_v2.types.sender_id_list.deserialize_aws_json_1_0(
                data["SenderIds"]
            )
        )
    if "Filters" in data:
        import capo_pinpoint_sms_voice_v2.types.sender_id_filter_list

        out["filters"] = (
            capo_pinpoint_sms_voice_v2.types.sender_id_filter_list.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "Owner" in data:
        out["owner"] = data["Owner"]
    return out
