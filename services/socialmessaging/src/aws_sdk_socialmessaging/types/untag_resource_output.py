"""Generated from Smithy shape ``com.amazonaws.socialmessaging#UntagResourceOutput``."""

from typing_extensions import NotRequired, TypedDict


class UntagResourceOutput(TypedDict, closed=True):
    status_code: NotRequired["int"]
    """<p>The status code of the untag resource operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceOutput) -> dict:
    out: dict = {}
    if "status_code" in value:
        out["statusCode"] = value["status_code"]
    return out


def deserialize_json(data: dict) -> UntagResourceOutput:
    out: UntagResourceOutput = {}  # type: ignore[typeddict-item]
    if "statusCode" in data:
        out["status_code"] = data["statusCode"]
    return out
