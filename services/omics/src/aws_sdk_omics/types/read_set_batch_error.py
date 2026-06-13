"""Generated from Smithy shape ``com.amazonaws.omics#ReadSetBatchError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.read_set_id


class ReadSetBatchError(TypedDict):
    id: "aws_sdk_omics.types.read_set_id.ReadSetId"
    """<p>The error's ID.</p>"""
    code: "str"
    """<p>The error's code.</p>"""
    message: "str"
    """<p>The error's message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadSetBatchError) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ReadSetBatchError:
    out: ReadSetBatchError = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ReadSetBatchError.id required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("ReadSetBatchError.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ReadSetBatchError.message required")
    return out
