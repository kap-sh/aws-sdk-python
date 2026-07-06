"""Generated from Smithy shape ``com.amazonaws.iot#UpdateCommandRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.command_description
    import aws_sdk_iot.types.command_id
    import aws_sdk_iot.types.deprecation_flag
    import aws_sdk_iot.types.display_name


class UpdateCommandRequest(TypedDict, closed=True):
    command_id: "aws_sdk_iot.types.command_id.CommandId"
    """<p>The unique identifier of the command to be updated.</p>"""
    display_name: NotRequired["aws_sdk_iot.types.display_name.DisplayName"]
    """<p>The new user-friendly name to use in the console for the command.</p>"""
    description: NotRequired["aws_sdk_iot.types.command_description.CommandDescription"]
    """<p>A short text description of the command.</p>"""
    deprecated: NotRequired["aws_sdk_iot.types.deprecation_flag.DeprecationFlag"]
    """<p>A boolean that you can use to specify whether to deprecate a command.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCommandRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "deprecated" in value:
        out["deprecated"] = value["deprecated"]
    return out


def deserialize_json(data: dict) -> UpdateCommandRequest:
    out: UpdateCommandRequest = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "description" in data:
        out["description"] = data["description"]
    if "deprecated" in data:
        out["deprecated"] = data["deprecated"]
    return out
