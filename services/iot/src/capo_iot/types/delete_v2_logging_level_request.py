"""Generated from Smithy shape ``com.amazonaws.iot#DeleteV2LoggingLevelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.log_target_name
    import capo_iot.types.log_target_type


class DeleteV2LoggingLevelRequest(TypedDict, closed=True):
    target_type: "capo_iot.types.log_target_type.LogTargetType"
    """<p>The type of resource for which you are configuring logging. Must be <code>THING_Group</code>.</p>"""
    target_name: "capo_iot.types.log_target_name.LogTargetName"
    """<p>The name of the resource for which you are configuring logging.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteV2LoggingLevelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteV2LoggingLevelRequest:
    out: DeleteV2LoggingLevelRequest = {}  # type: ignore[typeddict-item]
    return out
