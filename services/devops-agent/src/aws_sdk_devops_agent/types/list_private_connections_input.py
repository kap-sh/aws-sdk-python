"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListPrivateConnectionsInput``."""

from typing_extensions import TypedDict


class ListPrivateConnectionsInput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: ListPrivateConnectionsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPrivateConnectionsInput:
    out: ListPrivateConnectionsInput = {}  # type: ignore[typeddict-item]
    return out
