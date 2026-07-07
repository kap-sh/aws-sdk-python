"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeRcsAgentsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_information_list


class DescribeRcsAgentsResult(TypedDict, closed=True):
    rcs_agents: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_information_list.RcsAgentInformationList"
    ]
    """<p>An array of RcsAgentInformation objects that contain the details for the requested RCS agents.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. If this field is empty then there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRcsAgentsResult) -> dict:
    out: dict = {}
    if "rcs_agents" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_information_list

        out["RcsAgents"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_information_list.serialize_aws_json_1_0(
                value["rcs_agents"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRcsAgentsResult:
    out: DescribeRcsAgentsResult = {}  # type: ignore[typeddict-item]
    if "RcsAgents" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_information_list

        out["rcs_agents"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_information_list.deserialize_aws_json_1_0(
                data["RcsAgents"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
