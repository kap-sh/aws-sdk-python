"""Generated from Smithy shape ``com.amazonaws.iot#CommandSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.boolean_wrapper_object
    import aws_sdk_iot.types.command_arn
    import aws_sdk_iot.types.command_id
    import aws_sdk_iot.types.date_type
    import aws_sdk_iot.types.deprecation_flag
    import aws_sdk_iot.types.display_name


class CommandSummary(TypedDict):
    command_arn: NotRequired["aws_sdk_iot.types.command_arn.CommandArn"]
    """<p>The Amazon Resource Name (ARN) of the command.</p>"""
    command_id: NotRequired["aws_sdk_iot.types.command_id.CommandId"]
    """<p>The unique identifier of the command.</p>"""
    display_name: NotRequired["aws_sdk_iot.types.display_name.DisplayName"]
    """<p>The display name of the command.</p>"""
    deprecated: NotRequired["aws_sdk_iot.types.deprecation_flag.DeprecationFlag"]
    """<p>Indicates whether the command has been deprecated.</p>"""
    created_at: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The timestamp, when the command was created.</p>"""
    last_updated_at: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The timestamp, when the command was last updated.</p>"""
    pending_deletion: NotRequired[
        "aws_sdk_iot.types.boolean_wrapper_object.BooleanWrapperObject"
    ]
    """<p>Indicates whether the command is pending deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommandSummary) -> dict:
    out: dict = {}
    if "command_arn" in value:
        out["commandArn"] = value["command_arn"]
    if "command_id" in value:
        out["commandId"] = value["command_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "deprecated" in value:
        out["deprecated"] = value["deprecated"]
    if "created_at" in value:
        import aws_sdk_iot.types.date_type

        out["createdAt"] = aws_sdk_iot.types.date_type.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_iot.types.date_type

        out["lastUpdatedAt"] = aws_sdk_iot.types.date_type.serialize_json(
            value["last_updated_at"]
        )
    if "pending_deletion" in value:
        out["pendingDeletion"] = value["pending_deletion"]
    return out


def deserialize_json(data: dict) -> CommandSummary:
    out: CommandSummary = {}  # type: ignore[typeddict-item]
    if "commandArn" in data:
        out["command_arn"] = data["commandArn"]
    if "commandId" in data:
        out["command_id"] = data["commandId"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "deprecated" in data:
        out["deprecated"] = data["deprecated"]
    if "createdAt" in data:
        import aws_sdk_iot.types.date_type

        out["created_at"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_iot.types.date_type

        out["last_updated_at"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "pendingDeletion" in data:
        out["pending_deletion"] = data["pendingDeletion"]
    return out
