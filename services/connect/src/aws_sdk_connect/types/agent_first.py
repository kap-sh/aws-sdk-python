"""Generated from Smithy shape ``com.amazonaws.connect#AgentFirst``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.preview


class AgentFirst(TypedDict, closed=True):
    preview: NotRequired["aws_sdk_connect.types.preview.Preview"]
    """<p>Information about preview configuration of agent first outbound strategy</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentFirst) -> dict:
    out: dict = {}
    if "preview" in value:
        import aws_sdk_connect.types.preview

        out["Preview"] = aws_sdk_connect.types.preview.serialize_json(value["preview"])
    return out


def deserialize_json(data: dict) -> AgentFirst:
    out: AgentFirst = {}  # type: ignore[typeddict-item]
    if "Preview" in data:
        import aws_sdk_connect.types.preview

        out["preview"] = aws_sdk_connect.types.preview.deserialize_json(data["Preview"])
    return out
