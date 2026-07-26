"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ExportLensOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.lens_json


class ExportLensOutput(TypedDict, closed=True):
    lens_json: NotRequired["capo_wellarchitected.types.lens_json.LensJSON"]
    """<p>The JSON representation of a lens.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportLensOutput) -> dict:
    out: dict = {}
    if "lens_json" in value:
        out["LensJSON"] = value["lens_json"]
    return out


def deserialize_json(data: dict) -> ExportLensOutput:
    out: ExportLensOutput = {}  # type: ignore[typeddict-item]
    if "LensJSON" in data:
        out["lens_json"] = data["LensJSON"]
    return out
