"""Generated from Smithy shape ``com.amazonaws.mq#DeleteBrokerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__string


class DeleteBrokerRequest(TypedDict, closed=True):
    broker_id: "capo_mq.types.__string.__string"
    """<p>The unique ID that Amazon MQ generates for the broker.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBrokerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBrokerRequest:
    out: DeleteBrokerRequest = {}  # type: ignore[typeddict-item]
    return out
