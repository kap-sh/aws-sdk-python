"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeRcsAgentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.max_results
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.owner
    import aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_filter_list
    import aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_id_list


class DescribeRcsAgentsRequest(TypedDict):
    rcs_agent_ids: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_id_list.RcsAgentIdList"
    ]
    """<p>An array of unique identifiers for the RCS agents. This is an array of strings that can be either the RcsAgentId or RcsAgentArn.</p>"""
    owner: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.owner.Owner"]
    """<p>Use <code>SELF</code> to filter the list of RCS agents to ones your account owns or use <code>SHARED</code> to filter on RCS agents shared with your account. The <code>Owner</code> and <code>RcsAgentIds</code> parameters can't be used at the same time.</p>"""
    filters: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_filter_list.RcsAgentFilterList"
    ]
    """<p>An array of RcsAgentFilter objects to filter the results.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""
    max_results: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return per each request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRcsAgentsRequest) -> dict:
    out: dict = {}
    if "rcs_agent_ids" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_id_list

        out["RcsAgentIds"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_id_list.serialize_aws_json_1_0(
                value["rcs_agent_ids"]
            )
        )
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "filters" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_filter_list

        out["Filters"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_filter_list.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRcsAgentsRequest:
    out: DescribeRcsAgentsRequest = {}  # type: ignore[typeddict-item]
    if "RcsAgentIds" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_id_list

        out["rcs_agent_ids"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_id_list.deserialize_aws_json_1_0(
                data["RcsAgentIds"]
            )
        )
    if "Owner" in data:
        out["owner"] = data["Owner"]
    if "Filters" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_filter_list

        out["filters"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_filter_list.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
