"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AccessPreviewStatusReason``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.access_preview_status_reason_code


class AccessPreviewStatusReason(TypedDict, closed=True):
    code: "capo_accessanalyzer.types.access_preview_status_reason_code.AccessPreviewStatusReasonCode"
    """<p>The reason code for the current status of the access preview.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessPreviewStatusReason) -> dict:
    out: dict = {}
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> AccessPreviewStatusReason:
    out: AccessPreviewStatusReason = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("AccessPreviewStatusReason.code required")
    return out
