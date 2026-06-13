"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MessageDetail``."""

from typing import TypedDict

from typing_extensions import NotRequired


class MessageDetail(TypedDict):
    code: NotRequired["str"]
    """<p> The error code.</p>"""
    message: NotRequired["str"]
    """<p> The specific error message that MediaConnect returns to help you understand the reason that the request did not succeed.</p>"""
    resource_name: NotRequired["str"]
    """<p> The name of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageDetail) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    return out


def deserialize_json(data: dict) -> MessageDetail:
    out: MessageDetail = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    return out
