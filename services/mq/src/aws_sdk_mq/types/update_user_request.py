"""Generated from Smithy shape ``com.amazonaws.mq#UpdateUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mq.types.__boolean
    import aws_sdk_mq.types.__list_of__string
    import aws_sdk_mq.types.__string


class UpdateUserRequest(TypedDict):
    broker_id: "aws_sdk_mq.types.__string.__string"
    """<p>The unique ID that Amazon MQ generates for the broker.</p>"""
    console_access: NotRequired["aws_sdk_mq.types.__boolean.__boolean"]
    """<p>Enables access to the the ActiveMQ Web Console for the ActiveMQ user.</p>"""
    groups: NotRequired["aws_sdk_mq.types.__list_of__string.__listOf__string"]
    """<p>The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.</p>"""
    password: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The password of the user. This value must be at least 12 characters long, must contain at least 4 unique characters, and must not contain commas, colons, or equal signs (,:=).</p>"""
    username: "aws_sdk_mq.types.__string.__string"
    """<p>The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.</p>"""
    replication_user: NotRequired["aws_sdk_mq.types.__boolean.__boolean"]
    """<p>Defines whether the user is intended for data replication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserRequest) -> dict:
    out: dict = {}
    if "console_access" in value:
        out["consoleAccess"] = value["console_access"]
    if "groups" in value:
        import aws_sdk_mq.types.__list_of__string

        out["groups"] = aws_sdk_mq.types.__list_of__string.serialize_json(
            value["groups"]
        )
    if "password" in value:
        out["password"] = value["password"]
    if "replication_user" in value:
        out["replicationUser"] = value["replication_user"]
    return out


def deserialize_json(data: dict) -> UpdateUserRequest:
    out: UpdateUserRequest = {}  # type: ignore[typeddict-item]
    if "consoleAccess" in data:
        out["console_access"] = data["consoleAccess"]
    if "groups" in data:
        import aws_sdk_mq.types.__list_of__string

        out["groups"] = aws_sdk_mq.types.__list_of__string.deserialize_json(
            data["groups"]
        )
    if "password" in data:
        out["password"] = data["password"]
    if "replicationUser" in data:
        out["replication_user"] = data["replicationUser"]
    return out
