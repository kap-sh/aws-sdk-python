"""Generated from Smithy shape ``com.amazonaws.repostspace#BatchError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_repostspace.errors import DeserializationError

if TYPE_CHECKING:
    import capo_repostspace.types.accessor_id
    import capo_repostspace.types.error_code
    import capo_repostspace.types.error_message


class BatchError(TypedDict, closed=True):
    accessor_id: "capo_repostspace.types.accessor_id.AccessorId"
    """<p>The accessor identifier that's related to the error.</p>"""
    error: "capo_repostspace.types.error_code.ErrorCode"
    """<p>The error code.</p>"""
    message: "capo_repostspace.types.error_message.ErrorMessage"
    """<p>Description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchError) -> dict:
    out: dict = {}
    out["accessorId"] = value["accessor_id"]
    out["error"] = value["error"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchError:
    out: BatchError = {}  # type: ignore[typeddict-item]
    if "accessorId" in data:
        out["accessor_id"] = data["accessorId"]
    else:
        raise DeserializationError("BatchError.accessor_id required")
    if "error" in data:
        out["error"] = data["error"]
    else:
        raise DeserializationError("BatchError.error required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("BatchError.message required")
    return out
