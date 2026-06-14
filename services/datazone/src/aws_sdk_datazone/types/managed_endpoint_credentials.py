"""Generated from Smithy shape ``com.amazonaws.datazone#ManagedEndpointCredentials``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ManagedEndpointCredentials(TypedDict):
    id: NotRequired["str"]
    """<p>The identifier of the managed endpoint credentials.</p>"""
    token: NotRequired["str"]
    """<p>The ARN of the managed endpoint credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedEndpointCredentials) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "token" in value:
        out["token"] = value["token"]
    return out


def deserialize_json(data: dict) -> ManagedEndpointCredentials:
    out: ManagedEndpointCredentials = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "token" in data:
        out["token"] = data["token"]
    return out
