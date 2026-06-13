"""Generated from Smithy shape ``com.amazonaws.mgn#ExportErrorData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.large_bounded_string


class ExportErrorData(TypedDict):
    raw_error: NotRequired["aws_sdk_mgn.types.large_bounded_string.LargeBoundedString"]
    """<p>Export errors data raw error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportErrorData) -> dict:
    out: dict = {}
    if "raw_error" in value:
        out["rawError"] = value["raw_error"]
    return out


def deserialize_json(data: dict) -> ExportErrorData:
    out: ExportErrorData = {}  # type: ignore[typeddict-item]
    if "rawError" in data:
        out["raw_error"] = data["rawError"]
    return out
