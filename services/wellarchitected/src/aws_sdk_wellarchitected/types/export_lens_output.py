"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ExportLensOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_json


class ExportLensOutput(TypedDict):
    lens_json: NotRequired["aws_sdk_wellarchitected.types.lens_json.LensJSON"]
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
