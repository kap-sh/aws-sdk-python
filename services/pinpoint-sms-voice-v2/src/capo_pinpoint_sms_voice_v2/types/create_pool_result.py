"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CreatePoolResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.iam_role_arn
    import capo_pinpoint_sms_voice_v2.types.message_type
    import capo_pinpoint_sms_voice_v2.types.opt_out_list_name
    import capo_pinpoint_sms_voice_v2.types.pool_status
    import capo_pinpoint_sms_voice_v2.types.tag_list
    import capo_pinpoint_sms_voice_v2.types.two_way_channel_arn


class CreatePoolResult(TypedDict, closed=True):
    pool_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) for the pool.</p>"""
    pool_id: NotRequired["str"]
    """<p>The unique identifier for the pool.</p>"""
    status: NotRequired["capo_pinpoint_sms_voice_v2.types.pool_status.PoolStatus"]
    """<p>The current status of the pool.</p> <ul> <li> <p>CREATING: The pool is currently being created and isn't yet available for use.</p> </li> <li> <p>ACTIVE: The pool is active and available for use.</p> </li> <li> <p>DELETING: The pool is being deleted.</p> </li> </ul>"""
    message_type: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.message_type.MessageType"
    ]
    """<p>The type of message for the pool to use.</p>"""
    two_way_enabled: "bool"
    """<p>By default this is set to false. When set to true you can receive incoming text messages from your end recipients.</p>"""
    two_way_channel_arn: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.two_way_channel_arn.TwoWayChannelArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the two way channel.</p>"""
    two_way_channel_role: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.iam_role_arn.IamRoleArn"
    ]
    """<p>An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.</p>"""
    self_managed_opt_outs_enabled: "bool"
    """<p>By default this is set to false. When set to false, and an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, End User Messaging SMS automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.</p>"""
    opt_out_list_name: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.opt_out_list_name.OptOutListName"
    ]
    """<p>The name of the OptOutList associated with the pool.</p>"""
    shared_routes_enabled: "bool"
    """<p>Indicates whether shared routes are enabled for the pool. Set to false and only origination identities in this pool are used to send messages. </p>"""
    deletion_protection_enabled: "bool"
    """<p>When set to true deletion protection is enabled. By default this is set to false. </p>"""
    tags: NotRequired["capo_pinpoint_sms_voice_v2.types.tag_list.TagList"]
    """<p>An array of tags (key and value pairs) associated with the pool.</p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    r"""<p>The time when the pool was created, in <a href=\"https://www.epochconverter.com/\">UNIX epoch time</a> format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreatePoolResult) -> dict:
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
    out["DeletionProtectionEnabled"] = value.get("deletion_protection_enabled", False)
    if "tags" in value:
        import capo_pinpoint_sms_voice_v2.types.tag_list

        out["Tags"] = capo_pinpoint_sms_voice_v2.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "created_timestamp" in value:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["CreatedTimestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreatePoolResult:
    out: CreatePoolResult = {}  # type: ignore[typeddict-item]
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
    if "DeletionProtectionEnabled" in data:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    else:
        out["deletion_protection_enabled"] = False
    if "Tags" in data:
        import capo_pinpoint_sms_voice_v2.types.tag_list

        out["tags"] = (
            capo_pinpoint_sms_voice_v2.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    if "CreatedTimestamp" in data:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    return out
