"""Generated from Smithy shape ``com.amazonaws.iot#DeleteMitigationActionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.mitigation_action_name


class DeleteMitigationActionRequest(TypedDict):
    action_name: "aws_sdk_iot.types.mitigation_action_name.MitigationActionName"
    """<p>The name of the mitigation action that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMitigationActionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMitigationActionRequest:
    out: DeleteMitigationActionRequest = {}  # type: ignore[typeddict-item]
    return out
