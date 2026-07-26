"""Generated from Smithy shape ``com.amazonaws.mq#CreateBrokerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__string


class CreateBrokerResponse(TypedDict, closed=True):
    broker_arn: NotRequired["capo_mq.types.__string.__string"]
    """<p>The broker's Amazon Resource Name (ARN).</p>"""
    broker_id: NotRequired["capo_mq.types.__string.__string"]
    """<p>The unique ID that Amazon MQ generates for the broker.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBrokerResponse) -> dict:
    out: dict = {}
    if "broker_arn" in value:
        out["brokerArn"] = value["broker_arn"]
    if "broker_id" in value:
        out["brokerId"] = value["broker_id"]
    return out


def deserialize_json(data: dict) -> CreateBrokerResponse:
    out: CreateBrokerResponse = {}  # type: ignore[typeddict-item]
    if "brokerArn" in data:
        out["broker_arn"] = data["brokerArn"]
    if "brokerId" in data:
        out["broker_id"] = data["brokerId"]
    return out
