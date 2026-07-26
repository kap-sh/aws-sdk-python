"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeNotifyTemplatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.max_results
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.notify_template_filter_list
    import capo_pinpoint_sms_voice_v2.types.notify_template_id_list


class DescribeNotifyTemplatesRequest(TypedDict, closed=True):
    template_ids: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.notify_template_id_list.NotifyTemplateIdList"
    ]
    """<p>An array of template IDs to describe.</p>"""
    filters: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.notify_template_filter_list.NotifyTemplateFilterList"
    ]
    """<p>An array of NotifyTemplateFilter objects to filter the results on.</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""
    max_results: NotRequired["capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per each request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeNotifyTemplatesRequest) -> dict:
    out: dict = {}
    if "template_ids" in value:
        import capo_pinpoint_sms_voice_v2.types.notify_template_id_list

        out["TemplateIds"] = (
            capo_pinpoint_sms_voice_v2.types.notify_template_id_list.serialize_aws_json_1_0(
                value["template_ids"]
            )
        )
    if "filters" in value:
        import capo_pinpoint_sms_voice_v2.types.notify_template_filter_list

        out["Filters"] = (
            capo_pinpoint_sms_voice_v2.types.notify_template_filter_list.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeNotifyTemplatesRequest:
    out: DescribeNotifyTemplatesRequest = {}  # type: ignore[typeddict-item]
    if "TemplateIds" in data:
        import capo_pinpoint_sms_voice_v2.types.notify_template_id_list

        out["template_ids"] = (
            capo_pinpoint_sms_voice_v2.types.notify_template_id_list.deserialize_aws_json_1_0(
                data["TemplateIds"]
            )
        )
    if "Filters" in data:
        import capo_pinpoint_sms_voice_v2.types.notify_template_filter_list

        out["filters"] = (
            capo_pinpoint_sms_voice_v2.types.notify_template_filter_list.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
