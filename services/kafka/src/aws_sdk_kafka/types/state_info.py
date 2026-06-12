"""Generated from Smithy shape ``com.amazonaws.kafka#StateInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class StateInfo(TypedDict):
    code: NotRequired["aws_sdk_kafka.types.__string.__string"]
    message: NotRequired["aws_sdk_kafka.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: StateInfo) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> StateInfo:
    out: StateInfo = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    return out
