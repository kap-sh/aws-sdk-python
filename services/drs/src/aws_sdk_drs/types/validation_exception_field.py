"""Generated from Smithy shape ``com.amazonaws.drs#ValidationExceptionField``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_drs.types.large_bounded_string


class ValidationExceptionField(TypedDict):
    name: NotRequired["aws_sdk_drs.types.large_bounded_string.LargeBoundedString"]
    """<p>Validate exception field name.</p>"""
    message: NotRequired["aws_sdk_drs.types.large_bounded_string.LargeBoundedString"]
    """<p>Validate exception field message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionField) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "message" in data:
        out["message"] = data["message"]
    return out
