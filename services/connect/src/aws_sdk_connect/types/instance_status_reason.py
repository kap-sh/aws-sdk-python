"""Generated from Smithy shape ``com.amazonaws.connect#InstanceStatusReason``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.string


class InstanceStatusReason(TypedDict):
    message: NotRequired["aws_sdk_connect.types.string.String"]
    """<p>The message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceStatusReason) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InstanceStatusReason:
    out: InstanceStatusReason = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
