"""Generated from Smithy shape ``com.amazonaws.mq#DescribeUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__boolean
    import aws_sdk_mq.types.__list_of__string
    import aws_sdk_mq.types.__string
    import aws_sdk_mq.types.user_pending_changes


class DescribeUserResponse(TypedDict, closed=True):
    broker_id: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>Required. The unique ID that Amazon MQ generates for the broker.</p>"""
    console_access: NotRequired["aws_sdk_mq.types.__boolean.__boolean"]
    """<p>Enables access to the the ActiveMQ Web Console for the ActiveMQ user.</p>"""
    groups: NotRequired["aws_sdk_mq.types.__list_of__string.__listOf__string"]
    """<p>The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.</p>"""
    pending: NotRequired["aws_sdk_mq.types.user_pending_changes.UserPendingChanges"]
    """<p>The status of the changes pending for the ActiveMQ user.</p>"""
    username: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>Required. The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.</p>"""
    replication_user: NotRequired["aws_sdk_mq.types.__boolean.__boolean"]
    """<p>Describes whether the user is intended for data replication</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeUserResponse) -> dict:
    out: dict = {}
    if "broker_id" in value:
        out["brokerId"] = value["broker_id"]
    if "console_access" in value:
        out["consoleAccess"] = value["console_access"]
    if "groups" in value:
        import aws_sdk_mq.types.__list_of__string

        out["groups"] = aws_sdk_mq.types.__list_of__string.serialize_json(
            value["groups"]
        )
    if "pending" in value:
        import aws_sdk_mq.types.user_pending_changes

        out["pending"] = aws_sdk_mq.types.user_pending_changes.serialize_json(
            value["pending"]
        )
    if "username" in value:
        out["username"] = value["username"]
    if "replication_user" in value:
        out["replicationUser"] = value["replication_user"]
    return out


def deserialize_json(data: dict) -> DescribeUserResponse:
    out: DescribeUserResponse = {}  # type: ignore[typeddict-item]
    if "brokerId" in data:
        out["broker_id"] = data["brokerId"]
    if "consoleAccess" in data:
        out["console_access"] = data["consoleAccess"]
    if "groups" in data:
        import aws_sdk_mq.types.__list_of__string

        out["groups"] = aws_sdk_mq.types.__list_of__string.deserialize_json(
            data["groups"]
        )
    if "pending" in data:
        import aws_sdk_mq.types.user_pending_changes

        out["pending"] = aws_sdk_mq.types.user_pending_changes.deserialize_json(
            data["pending"]
        )
    if "username" in data:
        out["username"] = data["username"]
    if "replicationUser" in data:
        out["replication_user"] = data["replicationUser"]
    return out
