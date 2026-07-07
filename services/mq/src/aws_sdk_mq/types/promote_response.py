"""Generated from Smithy shape ``com.amazonaws.mq#PromoteResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__string


class PromoteResponse(TypedDict, closed=True):
    broker_id: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The unique ID that Amazon MQ generates for the broker.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromoteResponse) -> dict:
    out: dict = {}
    if "broker_id" in value:
        out["brokerId"] = value["broker_id"]
    return out


def deserialize_json(data: dict) -> PromoteResponse:
    out: PromoteResponse = {}  # type: ignore[typeddict-item]
    if "brokerId" in data:
        out["broker_id"] = data["brokerId"]
    return out
