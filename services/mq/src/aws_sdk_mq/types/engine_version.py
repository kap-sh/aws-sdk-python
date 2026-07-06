"""Generated from Smithy shape ``com.amazonaws.mq#EngineVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__string


class EngineVersion(TypedDict, closed=True):
    name: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>Id for the version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EngineVersion) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> EngineVersion:
    out: EngineVersion = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    return out
