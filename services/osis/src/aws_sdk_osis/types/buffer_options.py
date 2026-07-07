"""Generated from Smithy shape ``com.amazonaws.osis#BufferOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_osis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_osis.types.boolean


class BufferOptions(TypedDict, closed=True):
    persistent_buffer_enabled: "aws_sdk_osis.types.boolean.Boolean"
    """<p>Whether persistent buffering should be enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BufferOptions) -> dict:
    out: dict = {}
    out["PersistentBufferEnabled"] = value["persistent_buffer_enabled"]
    return out


def deserialize_json(data: dict) -> BufferOptions:
    out: BufferOptions = {}  # type: ignore[typeddict-item]
    if "PersistentBufferEnabled" in data:
        out["persistent_buffer_enabled"] = data["PersistentBufferEnabled"]
    else:
        raise DeserializationError("BufferOptions.persistent_buffer_enabled required")
    return out
