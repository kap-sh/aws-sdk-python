"""Generated from Smithy shape ``com.amazonaws.groundstation#DecodeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.json_string


class DecodeConfig(TypedDict, closed=True):
    unvalidated_json: "capo_groundstation.types.json_string.JsonString"
    """<p>Unvalidated JSON of a decode <code>Config</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DecodeConfig) -> dict:
    out: dict = {}
    out["unvalidatedJSON"] = value["unvalidated_json"]
    return out


def deserialize_json(data: dict) -> DecodeConfig:
    out: DecodeConfig = {}  # type: ignore[typeddict-item]
    if "unvalidatedJSON" in data:
        out["unvalidated_json"] = data["unvalidatedJSON"]
    else:
        raise DeserializationError("DecodeConfig.unvalidated_json required")
    return out
