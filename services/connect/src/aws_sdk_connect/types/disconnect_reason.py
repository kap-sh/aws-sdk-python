"""Generated from Smithy shape ``com.amazonaws.connect#DisconnectReason``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.disconnect_reason_code


class DisconnectReason(TypedDict):
    code: NotRequired[
        "aws_sdk_connect.types.disconnect_reason_code.DisconnectReasonCode"
    ]
    """<p>A code that indicates how the contact was terminated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisconnectReason) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    return out


def deserialize_json(data: dict) -> DisconnectReason:
    out: DisconnectReason = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    return out
