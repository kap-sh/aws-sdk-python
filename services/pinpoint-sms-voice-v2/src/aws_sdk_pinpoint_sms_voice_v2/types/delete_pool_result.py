"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeletePoolResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_pinpoint_sms_voice_v2.types.iam_role_arn
    import aws_sdk_pinpoint_sms_voice_v2.types.message_type
    import aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_name
    import aws_sdk_pinpoint_sms_voice_v2.types.pool_status
    import aws_sdk_pinpoint_sms_voice_v2.types.two_way_channel_arn


class DeletePoolResult(TypedDict):
    pool_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the pool that was deleted.</p>"""
    pool_id: NotRequired["str"]
    """<p>The PoolId of the pool that was deleted.</p>"""
    status: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.pool_status.PoolStatus"]
    """<p>The current status of the pool.</p> <ul> <li> <p>CREATING: The pool is currently being created and isn't yet available for use.</p> </li> <li> <p>ACTIVE: The pool is active and available for use.</p> </li> <li> <p>DELETING: The pool is being deleted.</p> </li> </ul>"""
    message_type: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.message_type.MessageType"
    ]
    """<p>The message type that was associated with the deleted pool.</p>"""
    two_way_enabled: "bool"
    """<p>By default this is set to false. When set to true you can receive incoming text messages from your end recipients.</p>"""
    two_way_channel_arn: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.two_way_channel_arn.TwoWayChannelArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the TwoWayChannel.</p>"""
    two_way_channel_role: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.iam_role_arn.IamRoleArn"
    ]
    """<p>An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.</p>"""
    self_managed_opt_outs_enabled: "bool"
    """<p>By default this is set to false. When set to false and an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, End User Messaging SMS automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.</p>"""
    opt_out_list_name: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_name.OptOutListName"
    ]
    """<p>The name of the OptOutList that was associated with the deleted pool.</p>"""
    shared_routes_enabled: "bool"
    """<p>Indicates whether shared routes are enabled for the pool.</p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    """<p>The time when the pool was created, in <a href=\"https://www.epochconverter.com/\">UNIX epoch time</a> format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeletePoolResult) -> dict:
    out: dict = {}
    if "pool_arn" in value:
        out["PoolArn"] = value["pool_arn"]
    if "pool_id" in value:
        out["PoolId"] = value["pool_id"]
    if "status" in value:
        out["Status"] = value["status"]
    if "message_type" in value:
        out["MessageType"] = value["message_type"]
    out["TwoWayEnabled"] = value.get("two_way_enabled", False)
    if "two_way_channel_arn" in value:
        out["TwoWayChannelArn"] = value["two_way_channel_arn"]
    if "two_way_channel_role" in value:
        out["TwoWayChannelRole"] = value["two_way_channel_role"]
    out["SelfManagedOptOutsEnabled"] = value.get("self_managed_opt_outs_enabled", False)
    if "opt_out_list_name" in value:
        out["OptOutListName"] = value["opt_out_list_name"]
    out["SharedRoutesEnabled"] = value.get("shared_routes_enabled", False)
    if "created_timestamp" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["CreatedTimestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeletePoolResult:
    out: DeletePoolResult = {}  # type: ignore[typeddict-item]
    if "PoolArn" in data:
        out["pool_arn"] = data["PoolArn"]
    if "PoolId" in data:
        out["pool_id"] = data["PoolId"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "MessageType" in data:
        out["message_type"] = data["MessageType"]
    if "TwoWayEnabled" in data:
        out["two_way_enabled"] = data["TwoWayEnabled"]
    else:
        out["two_way_enabled"] = False
    if "TwoWayChannelArn" in data:
        out["two_way_channel_arn"] = data["TwoWayChannelArn"]
    if "TwoWayChannelRole" in data:
        out["two_way_channel_role"] = data["TwoWayChannelRole"]
    if "SelfManagedOptOutsEnabled" in data:
        out["self_managed_opt_outs_enabled"] = data["SelfManagedOptOutsEnabled"]
    else:
        out["self_managed_opt_outs_enabled"] = False
    if "OptOutListName" in data:
        out["opt_out_list_name"] = data["OptOutListName"]
    if "SharedRoutesEnabled" in data:
        out["shared_routes_enabled"] = data["SharedRoutesEnabled"]
    else:
        out["shared_routes_enabled"] = False
    if "CreatedTimestamp" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    return out
