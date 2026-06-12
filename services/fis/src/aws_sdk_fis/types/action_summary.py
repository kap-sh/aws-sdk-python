"""Generated from Smithy shape ``com.amazonaws.fis#ActionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fis.types.action_description
    import aws_sdk_fis.types.action_id
    import aws_sdk_fis.types.action_target_map
    import aws_sdk_fis.types.resource_arn
    import aws_sdk_fis.types.tag_map


class ActionSummary(TypedDict):
    id: NotRequired["aws_sdk_fis.types.action_id.ActionId"]
    """<p>The ID of the action.</p>"""
    arn: NotRequired["aws_sdk_fis.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the action.</p>"""
    description: NotRequired["aws_sdk_fis.types.action_description.ActionDescription"]
    """<p>The description for the action.</p>"""
    targets: NotRequired["aws_sdk_fis.types.action_target_map.ActionTargetMap"]
    """<p>The targets for the action.</p>"""
    tags: NotRequired["aws_sdk_fis.types.tag_map.TagMap"]
    """<p>The tags for the action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "targets" in value:
        import aws_sdk_fis.types.action_target_map

        out["targets"] = aws_sdk_fis.types.action_target_map.serialize_json(
            value["targets"]
        )
    if "tags" in value:
        import aws_sdk_fis.types.tag_map

        out["tags"] = aws_sdk_fis.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ActionSummary:
    out: ActionSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "description" in data:
        out["description"] = data["description"]
    if "targets" in data:
        import aws_sdk_fis.types.action_target_map

        out["targets"] = aws_sdk_fis.types.action_target_map.deserialize_json(
            data["targets"]
        )
    if "tags" in data:
        import aws_sdk_fis.types.tag_map

        out["tags"] = aws_sdk_fis.types.tag_map.deserialize_json(data["tags"])
    return out
