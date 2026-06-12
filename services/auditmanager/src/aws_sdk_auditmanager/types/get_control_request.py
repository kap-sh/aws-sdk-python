"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetControlRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.uuid


class GetControlRequest(TypedDict):
    control_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The identifier for the control. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetControlRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetControlRequest:
    out: GetControlRequest = {}  # type: ignore[typeddict-item]
    return out
