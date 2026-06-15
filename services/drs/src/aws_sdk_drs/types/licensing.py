"""Generated from Smithy shape ``com.amazonaws.drs#Licensing``."""

from typing import TypedDict

from typing_extensions import NotRequired


class Licensing(TypedDict):
    os_byol: NotRequired["bool"]
    r"""<p>Whether to enable \"Bring your own license\" or not.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Licensing) -> dict:
    out: dict = {}
    if "os_byol" in value:
        out["osByol"] = value["os_byol"]
    return out


def deserialize_json(data: dict) -> Licensing:
    out: Licensing = {}  # type: ignore[typeddict-item]
    if "osByol" in data:
        out["os_byol"] = data["osByol"]
    return out
