"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ComponentState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.component_status
    import capo_imagebuilder.types.non_empty_string


class ComponentState(TypedDict, closed=True):
    status: NotRequired["capo_imagebuilder.types.component_status.ComponentStatus"]
    """<p>The current state of the component.</p>"""
    reason: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>Describes how or why the component changed state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentState) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_imagebuilder.types.component_status

        out["status"] = capo_imagebuilder.types.component_status.serialize_json(
            value["status"]
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> ComponentState:
    out: ComponentState = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_imagebuilder.types.component_status

        out["status"] = capo_imagebuilder.types.component_status.deserialize_json(
            data["status"]
        )
    if "reason" in data:
        out["reason"] = data["reason"]
    return out
