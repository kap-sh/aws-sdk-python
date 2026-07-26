"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#StatusDetails``."""

from typing_extensions import NotRequired, TypedDict


class StatusDetails(TypedDict, closed=True):
    status_code: NotRequired["str"]
    """<p>The status code that was returned. The status code is intended for programmatic error handling. Clean Rooms ML will not change the status code for existing error conditions.</p>"""
    message: NotRequired["str"]
    """<p>The error message that was returned. The message is intended for human consumption and can change at any time. Use the <code>statusCode</code> for programmatic error handling.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatusDetails) -> dict:
    out: dict = {}
    if "status_code" in value:
        out["statusCode"] = value["status_code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> StatusDetails:
    out: StatusDetails = {}  # type: ignore[typeddict-item]
    if "statusCode" in data:
        out["status_code"] = data["statusCode"]
    if "message" in data:
        out["message"] = data["message"]
    return out
