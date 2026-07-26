"""Generated from Smithy shape ``com.amazonaws.socialmessaging#TagResourceOutput``."""

from typing_extensions import NotRequired, TypedDict


class TagResourceOutput(TypedDict, closed=True):
    status_code: NotRequired["int"]
    """<p>The status code of the tag resource operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceOutput) -> dict:
    out: dict = {}
    if "status_code" in value:
        out["statusCode"] = value["status_code"]
    return out


def deserialize_json(data: dict) -> TagResourceOutput:
    out: TagResourceOutput = {}  # type: ignore[typeddict-item]
    if "statusCode" in data:
        out["status_code"] = data["statusCode"]
    return out
