"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ActionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.resolve_to
    import capo_iotsitewise.types.target_resource


class ActionSummary(TypedDict, closed=True):
    action_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the action.</p>"""
    action_definition_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the action definition.</p>"""
    target_resource: NotRequired[
        "capo_iotsitewise.types.target_resource.TargetResource"
    ]
    """<p>The resource the action will be taken on.</p>"""
    resolve_to: NotRequired["capo_iotsitewise.types.resolve_to.ResolveTo"]
    """<p>The detailed resource this action resolves to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionSummary) -> dict:
    out: dict = {}
    if "action_id" in value:
        out["actionId"] = value["action_id"]
    if "action_definition_id" in value:
        out["actionDefinitionId"] = value["action_definition_id"]
    if "target_resource" in value:
        import capo_iotsitewise.types.target_resource

        out["targetResource"] = capo_iotsitewise.types.target_resource.serialize_json(
            value["target_resource"]
        )
    if "resolve_to" in value:
        import capo_iotsitewise.types.resolve_to

        out["resolveTo"] = capo_iotsitewise.types.resolve_to.serialize_json(
            value["resolve_to"]
        )
    return out


def deserialize_json(data: dict) -> ActionSummary:
    out: ActionSummary = {}  # type: ignore[typeddict-item]
    if "actionId" in data:
        out["action_id"] = data["actionId"]
    if "actionDefinitionId" in data:
        out["action_definition_id"] = data["actionDefinitionId"]
    if "targetResource" in data:
        import capo_iotsitewise.types.target_resource

        out["target_resource"] = (
            capo_iotsitewise.types.target_resource.deserialize_json(
                data["targetResource"]
            )
        )
    if "resolveTo" in data:
        import capo_iotsitewise.types.resolve_to

        out["resolve_to"] = capo_iotsitewise.types.resolve_to.deserialize_json(
            data["resolveTo"]
        )
    return out
