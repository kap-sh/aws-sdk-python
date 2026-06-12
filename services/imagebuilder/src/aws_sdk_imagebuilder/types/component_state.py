"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ComponentState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.component_status
    import aws_sdk_imagebuilder.types.non_empty_string


class ComponentState(TypedDict):
    status: NotRequired["aws_sdk_imagebuilder.types.component_status.ComponentStatus"]
    """<p>The current state of the component.</p>"""
    reason: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>Describes how or why the component changed state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentState) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_imagebuilder.types.component_status

        out["status"] = aws_sdk_imagebuilder.types.component_status.serialize_json(
            value["status"]
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> ComponentState:
    out: ComponentState = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_imagebuilder.types.component_status

        out["status"] = aws_sdk_imagebuilder.types.component_status.deserialize_json(
            data["status"]
        )
    if "reason" in data:
        out["reason"] = data["reason"]
    return out
