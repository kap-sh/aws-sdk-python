"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteRcsAgentResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_pinpoint_sms_voice_v2.types.iam_role_arn
    import aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_name
    import aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_status
    import aws_sdk_pinpoint_sms_voice_v2.types.two_way_channel_arn


class DeleteRcsAgentResult(TypedDict):
    rcs_agent_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the deleted RCS agent.</p>"""
    rcs_agent_id: "str"
    """<p>The unique identifier for the deleted RCS agent.</p>"""
    status: "aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_status.RcsAgentStatus"
    """<p>The current status of the RCS agent.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The time when the RCS agent was created, in <a href=\"https://www.epochconverter.com/\">UNIX epoch time</a> format.</p>"""
    deletion_protection_enabled: "bool"
    """<p>When set to true deletion protection is enabled. By default this is set to false.</p>"""
    opt_out_list_name: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_name.OptOutListName"
    ]
    """<p>The name of the OptOutList that was associated with the deleted RCS agent.</p>"""
    self_managed_opt_outs_enabled: "bool"
    """<p>By default this is set to false. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.</p>"""
    two_way_channel_arn: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.two_way_channel_arn.TwoWayChannelArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the two way channel.</p>"""
    two_way_channel_role: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.iam_role_arn.IamRoleArn"
    ]
    """<p>An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.</p>"""
    two_way_enabled: "bool"
    """<p>By default this is set to false. When set to true you can receive incoming text messages from your end recipients.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRcsAgentResult) -> dict:
    out: dict = {}
    out["RcsAgentArn"] = value["rcs_agent_arn"]
    out["RcsAgentId"] = value["rcs_agent_id"]
    out["Status"] = value["status"]
    import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    out["DeletionProtectionEnabled"] = value.get("deletion_protection_enabled", False)
    if "opt_out_list_name" in value:
        out["OptOutListName"] = value["opt_out_list_name"]
    out["SelfManagedOptOutsEnabled"] = value.get("self_managed_opt_outs_enabled", False)
    if "two_way_channel_arn" in value:
        out["TwoWayChannelArn"] = value["two_way_channel_arn"]
    if "two_way_channel_role" in value:
        out["TwoWayChannelRole"] = value["two_way_channel_role"]
    out["TwoWayEnabled"] = value.get("two_way_enabled", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRcsAgentResult:
    out: DeleteRcsAgentResult = {}  # type: ignore[typeddict-item]
    if "RcsAgentArn" in data:
        out["rcs_agent_arn"] = data["RcsAgentArn"]
    else:
        raise DeserializationError("DeleteRcsAgentResult.rcs_agent_arn required")
    if "RcsAgentId" in data:
        out["rcs_agent_id"] = data["RcsAgentId"]
    else:
        raise DeserializationError("DeleteRcsAgentResult.rcs_agent_id required")
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("DeleteRcsAgentResult.status required")
    if "CreatedTimestamp" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        raise DeserializationError("DeleteRcsAgentResult.created_timestamp required")
    if "DeletionProtectionEnabled" in data:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    else:
        out["deletion_protection_enabled"] = False
    if "OptOutListName" in data:
        out["opt_out_list_name"] = data["OptOutListName"]
    if "SelfManagedOptOutsEnabled" in data:
        out["self_managed_opt_outs_enabled"] = data["SelfManagedOptOutsEnabled"]
    else:
        out["self_managed_opt_outs_enabled"] = False
    if "TwoWayChannelArn" in data:
        out["two_way_channel_arn"] = data["TwoWayChannelArn"]
    if "TwoWayChannelRole" in data:
        out["two_way_channel_role"] = data["TwoWayChannelRole"]
    if "TwoWayEnabled" in data:
        out["two_way_enabled"] = data["TwoWayEnabled"]
    else:
        out["two_way_enabled"] = False
    return out
