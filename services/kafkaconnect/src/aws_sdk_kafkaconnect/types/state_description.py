"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#StateDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string


class StateDescription(TypedDict, closed=True):
    code: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>A code that describes the state of a resource.</p>"""
    message: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>A message that describes the state of a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StateDescription) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> StateDescription:
    out: StateDescription = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    return out
