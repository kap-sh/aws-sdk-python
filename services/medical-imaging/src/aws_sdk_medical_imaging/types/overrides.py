"""Generated from Smithy shape ``com.amazonaws.medicalimaging#Overrides``."""

from typing import TypedDict

from typing_extensions import NotRequired


class Overrides(TypedDict):
    forced: NotRequired["bool"]
    """<p>Providing this parameter will force completion of the <code>CopyImageSet</code> and <code>UpdateImageSetMetadata</code> actions, even if metadata is inconsistent at the Patient, Study, and/or Series levels.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Overrides) -> dict:
    out: dict = {}
    if "forced" in value:
        out["forced"] = value["forced"]
    return out


def deserialize_json(data: dict) -> Overrides:
    out: Overrides = {}  # type: ignore[typeddict-item]
    if "forced" in data:
        out["forced"] = data["forced"]
    return out
