"""Generated from Smithy shape ``com.amazonaws.neptunedata#DeleteMLEndpointOutput``."""

from typing_extensions import NotRequired, TypedDict


class DeleteMLEndpointOutput(TypedDict, closed=True):
    status: NotRequired["str"]
    """<p>The status of the cancellation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMLEndpointOutput) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> DeleteMLEndpointOutput:
    out: DeleteMLEndpointOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    return out
