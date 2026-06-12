"""Generated from Smithy shape ``com.amazonaws.iot#UpdateCommandResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.command_description
    import aws_sdk_iot.types.command_id
    import aws_sdk_iot.types.date_type
    import aws_sdk_iot.types.deprecation_flag
    import aws_sdk_iot.types.display_name


class UpdateCommandResponse(TypedDict):
    command_id: NotRequired["aws_sdk_iot.types.command_id.CommandId"]
    """<p>The unique identifier of the command.</p>"""
    display_name: NotRequired["aws_sdk_iot.types.display_name.DisplayName"]
    """<p>The updated user-friendly display name in the console for the command.</p>"""
    description: NotRequired["aws_sdk_iot.types.command_description.CommandDescription"]
    """<p>The updated text description of the command.</p>"""
    deprecated: NotRequired["aws_sdk_iot.types.deprecation_flag.DeprecationFlag"]
    """<p>The boolean that indicates whether the command was deprecated.</p>"""
    last_updated_at: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The date and time (epoch timestamp in seconds) when the command was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCommandResponse) -> dict:
    out: dict = {}
    if "command_id" in value:
        out["commandId"] = value["command_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "deprecated" in value:
        out["deprecated"] = value["deprecated"]
    if "last_updated_at" in value:
        import aws_sdk_iot.types.date_type

        out["lastUpdatedAt"] = aws_sdk_iot.types.date_type.serialize_json(
            value["last_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> UpdateCommandResponse:
    out: UpdateCommandResponse = {}  # type: ignore[typeddict-item]
    if "commandId" in data:
        out["command_id"] = data["commandId"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "description" in data:
        out["description"] = data["description"]
    if "deprecated" in data:
        out["deprecated"] = data["deprecated"]
    if "lastUpdatedAt" in data:
        import aws_sdk_iot.types.date_type

        out["last_updated_at"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["lastUpdatedAt"]
        )
    return out
