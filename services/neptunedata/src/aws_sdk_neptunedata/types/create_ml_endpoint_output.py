"""Generated from Smithy shape ``com.amazonaws.neptunedata#CreateMLEndpointOutput``."""

from typing import TypedDict

from typing_extensions import NotRequired


class CreateMLEndpointOutput(TypedDict):
    id: NotRequired["str"]
    """<p>The unique ID of the new inference endpoint.</p>"""
    arn: NotRequired["str"]
    """<p>The ARN for the new inference endpoint.</p>"""
    creation_time_in_millis: NotRequired["int"]
    """<p>The endpoint creation time, in milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMLEndpointOutput) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "creation_time_in_millis" in value:
        out["creationTimeInMillis"] = value["creation_time_in_millis"]
    return out


def deserialize_json(data: dict) -> CreateMLEndpointOutput:
    out: CreateMLEndpointOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "creationTimeInMillis" in data:
        out["creation_time_in_millis"] = data["creationTimeInMillis"]
    return out
