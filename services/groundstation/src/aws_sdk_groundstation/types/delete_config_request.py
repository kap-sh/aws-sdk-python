"""Generated from Smithy shape ``com.amazonaws.groundstation#DeleteConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.config_capability_type
    import aws_sdk_groundstation.types.uuid


class DeleteConfigRequest(TypedDict, closed=True):
    config_id: "aws_sdk_groundstation.types.uuid.Uuid"
    """<p>UUID of a <code>Config</code>.</p>"""
    config_type: (
        "aws_sdk_groundstation.types.config_capability_type.ConfigCapabilityType"
    )
    """<p>Type of a <code>Config</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfigRequest:
    out: DeleteConfigRequest = {}  # type: ignore[typeddict-item]
    return out
