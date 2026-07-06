"""Generated from Smithy shape ``com.amazonaws.mq#RebootBrokerResponse``."""

from typing_extensions import TypedDict


class RebootBrokerResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: RebootBrokerResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RebootBrokerResponse:
    out: RebootBrokerResponse = {}  # type: ignore[typeddict-item]
    return out
