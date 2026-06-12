"""Generated from Smithy shape ``com.amazonaws.auditmanager#DeleteControlRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.uuid


class DeleteControlRequest(TypedDict):
    control_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the control. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteControlRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteControlRequest:
    out: DeleteControlRequest = {}  # type: ignore[typeddict-item]
    return out
