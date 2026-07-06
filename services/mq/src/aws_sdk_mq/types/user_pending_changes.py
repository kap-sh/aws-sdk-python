"""Generated from Smithy shape ``com.amazonaws.mq#UserPendingChanges``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__boolean
    import aws_sdk_mq.types.__list_of__string
    import aws_sdk_mq.types.change_type


class UserPendingChanges(TypedDict, closed=True):
    console_access: NotRequired["aws_sdk_mq.types.__boolean.__boolean"]
    """<p>Enables access to the the ActiveMQ Web Console for the ActiveMQ user.</p>"""
    groups: NotRequired["aws_sdk_mq.types.__list_of__string.__listOf__string"]
    """<p>The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.</p>"""
    pending_change: NotRequired["aws_sdk_mq.types.change_type.ChangeType"]
    """<p>Required. The type of change pending for the ActiveMQ user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserPendingChanges) -> dict:
    out: dict = {}
    if "console_access" in value:
        out["consoleAccess"] = value["console_access"]
    if "groups" in value:
        import aws_sdk_mq.types.__list_of__string

        out["groups"] = aws_sdk_mq.types.__list_of__string.serialize_json(
            value["groups"]
        )
    if "pending_change" in value:
        import aws_sdk_mq.types.change_type

        out["pendingChange"] = aws_sdk_mq.types.change_type.serialize_json(
            value["pending_change"]
        )
    return out


def deserialize_json(data: dict) -> UserPendingChanges:
    out: UserPendingChanges = {}  # type: ignore[typeddict-item]
    if "consoleAccess" in data:
        out["console_access"] = data["consoleAccess"]
    if "groups" in data:
        import aws_sdk_mq.types.__list_of__string

        out["groups"] = aws_sdk_mq.types.__list_of__string.deserialize_json(
            data["groups"]
        )
    if "pendingChange" in data:
        import aws_sdk_mq.types.change_type

        out["pending_change"] = aws_sdk_mq.types.change_type.deserialize_json(
            data["pendingChange"]
        )
    return out
