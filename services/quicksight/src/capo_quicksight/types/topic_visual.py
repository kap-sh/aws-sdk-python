"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicVisual``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.limited_string
    import capo_quicksight.types.topic_ir
    import capo_quicksight.types.topic_visuals
    import capo_quicksight.types.visual_role


class TopicVisual(TypedDict, closed=True):
    visual_id: NotRequired["capo_quicksight.types.limited_string.LimitedString"]
    """<p>The visual ID for the <code>TopicVisual</code>.</p>"""
    role: NotRequired["capo_quicksight.types.visual_role.VisualRole"]
    """<p>The role for the <code>TopicVisual</code>.</p>"""
    ir: NotRequired["capo_quicksight.types.topic_ir.TopicIR"]
    """<p>The ir for the <code>TopicVisual</code>.</p>"""
    supporting_visuals: NotRequired["capo_quicksight.types.topic_visuals.TopicVisuals"]
    """<p>The supporting visuals for the <code>TopicVisual</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicVisual) -> dict:
    out: dict = {}
    if "visual_id" in value:
        out["VisualId"] = value["visual_id"]
    if "role" in value:
        import capo_quicksight.types.visual_role

        out["Role"] = capo_quicksight.types.visual_role.serialize_json(value["role"])
    if "ir" in value:
        import capo_quicksight.types.topic_ir

        out["Ir"] = capo_quicksight.types.topic_ir.serialize_json(value["ir"])
    if "supporting_visuals" in value:
        import capo_quicksight.types.topic_visuals

        out["SupportingVisuals"] = capo_quicksight.types.topic_visuals.serialize_json(
            value["supporting_visuals"]
        )
    return out


def deserialize_json(data: dict) -> TopicVisual:
    out: TopicVisual = {}  # type: ignore[typeddict-item]
    if "VisualId" in data:
        out["visual_id"] = data["VisualId"]
    if "Role" in data:
        import capo_quicksight.types.visual_role

        out["role"] = capo_quicksight.types.visual_role.deserialize_json(data["Role"])
    if "Ir" in data:
        import capo_quicksight.types.topic_ir

        out["ir"] = capo_quicksight.types.topic_ir.deserialize_json(data["Ir"])
    if "SupportingVisuals" in data:
        import capo_quicksight.types.topic_visuals

        out["supporting_visuals"] = (
            capo_quicksight.types.topic_visuals.deserialize_json(
                data["SupportingVisuals"]
            )
        )
    return out
