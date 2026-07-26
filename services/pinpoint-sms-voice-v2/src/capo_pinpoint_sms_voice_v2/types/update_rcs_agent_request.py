"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#UpdateRcsAgentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.iam_role_arn
    import capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn
    import capo_pinpoint_sms_voice_v2.types.rcs_agent_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.two_way_channel_arn


class UpdateRcsAgentRequest(TypedDict, closed=True):
    rcs_agent_id: "capo_pinpoint_sms_voice_v2.types.rcs_agent_id_or_arn.RcsAgentIdOrArn"
    """<p>The unique identifier of the RCS agent to update. You can use either the RcsAgentId or RcsAgentArn.</p>"""
    deletion_protection_enabled: NotRequired["bool"]
    """<p>By default this is set to false. When set to true the RCS agent can't be deleted.</p>"""
    opt_out_list_name: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn.OptOutListNameOrArn"
    ]
    """<p>The OptOutList to associate with the RCS agent. Valid values are either OptOutListName or OptOutListArn.</p>"""
    self_managed_opt_outs_enabled: NotRequired["bool"]
    """<p>By default this is set to false. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.</p>"""
    two_way_channel_arn: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.two_way_channel_arn.TwoWayChannelArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the two way channel.</p>"""
    two_way_channel_role: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.iam_role_arn.IamRoleArn"
    ]
    """<p>An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.</p>"""
    two_way_enabled: NotRequired["bool"]
    """<p>By default this is set to false. When set to true you can receive incoming text messages from your end recipients.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateRcsAgentRequest) -> dict:
    out: dict = {}
    out["RcsAgentId"] = value["rcs_agent_id"]
    if "deletion_protection_enabled" in value:
        out["DeletionProtectionEnabled"] = value["deletion_protection_enabled"]
    if "opt_out_list_name" in value:
        out["OptOutListName"] = value["opt_out_list_name"]
    if "self_managed_opt_outs_enabled" in value:
        out["SelfManagedOptOutsEnabled"] = value["self_managed_opt_outs_enabled"]
    if "two_way_channel_arn" in value:
        out["TwoWayChannelArn"] = value["two_way_channel_arn"]
    if "two_way_channel_role" in value:
        out["TwoWayChannelRole"] = value["two_way_channel_role"]
    if "two_way_enabled" in value:
        out["TwoWayEnabled"] = value["two_way_enabled"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateRcsAgentRequest:
    out: UpdateRcsAgentRequest = {}  # type: ignore[typeddict-item]
    if "RcsAgentId" in data:
        out["rcs_agent_id"] = data["RcsAgentId"]
    else:
        raise DeserializationError("UpdateRcsAgentRequest.rcs_agent_id required")
    if "DeletionProtectionEnabled" in data:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    if "OptOutListName" in data:
        out["opt_out_list_name"] = data["OptOutListName"]
    if "SelfManagedOptOutsEnabled" in data:
        out["self_managed_opt_outs_enabled"] = data["SelfManagedOptOutsEnabled"]
    if "TwoWayChannelArn" in data:
        out["two_way_channel_arn"] = data["TwoWayChannelArn"]
    if "TwoWayChannelRole" in data:
        out["two_way_channel_role"] = data["TwoWayChannelRole"]
    if "TwoWayEnabled" in data:
        out["two_way_enabled"] = data["TwoWayEnabled"]
    return out
