"""Generated from Smithy shape ``com.amazonaws.polly#FlushStreamConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_polly.types.force


class FlushStreamConfiguration(TypedDict):
    force: "aws_sdk_polly.types.force.Force"
    """<p>Specifies whether to force the synthesis engine to immediately write buffered audio data to the output stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlushStreamConfiguration) -> dict:
    out: dict = {}
    out["Force"] = value.get("force", False)
    return out


def deserialize_json(data: dict) -> FlushStreamConfiguration:
    out: FlushStreamConfiguration = {}  # type: ignore[typeddict-item]
    if "Force" in data:
        out["force"] = data["Force"]
    else:
        out["force"] = False
    return out
