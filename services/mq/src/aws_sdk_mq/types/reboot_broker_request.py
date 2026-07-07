"""Generated from Smithy shape ``com.amazonaws.mq#RebootBrokerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__string


class RebootBrokerRequest(TypedDict, closed=True):
    broker_id: "aws_sdk_mq.types.__string.__string"
    """<p>The unique ID that Amazon MQ generates for the broker.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RebootBrokerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RebootBrokerRequest:
    out: RebootBrokerRequest = {}  # type: ignore[typeddict-item]
    return out
