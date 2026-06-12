"""Generated from Smithy shape ``com.amazonaws.opensearch#ValidationFailure``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.string


class ValidationFailure(TypedDict):
    code: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>The error code of the failure.</p>"""
    message: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>A message corresponding to the failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationFailure) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationFailure:
    out: ValidationFailure = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
